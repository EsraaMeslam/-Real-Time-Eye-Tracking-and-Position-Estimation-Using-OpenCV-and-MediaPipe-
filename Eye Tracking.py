import cv2
import mediapipe as mp
import numpy as np
import utils

LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture("eye.mp4")

def landmark_detect(img, res, draw=False):
    height = img.shape[0]
    width = img.shape[1]
    mesh_coor = [(int(point.x * width), int(point.y * height)) for point in res.multi_face_landmarks[0].landmark]
    if draw:
        [cv2.circle(img, p, 2, (0, 255, 0), -1) for p in mesh_coor]
    return mesh_coor

def ecul_dis(point, point1):
    x, y = point
    x1, y1 = point1
    dis = np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return dis

def eyes_extractor(img, right_eye_corr, left_eye_corr):
    cv2.polylines(img, [np.array(right_eye_corr, dtype=np.int32)], True, (0, 255, 0), 1)
    cv2.polylines(img, [np.array(left_eye_corr, dtype=np.int32)], True, (0, 255, 0), 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dim = gray.shape
    mask = np.zeros(dim, dtype=np.uint8)

    cv2.fillPoly(mask, [np.array(right_eye_corr, dtype=np.int32)], 255)
    cv2.fillPoly(mask, [np.array(left_eye_corr, dtype=np.int32)], 255)

    eyes = cv2.bitwise_and(gray, gray, mask=mask)
    cv2.imshow("Eye Draw", eyes)
    eyes[mask == 0] = 155

    r_min_x = min(right_eye_corr, key=lambda item: item[0])[0]
    r_max_x = max(right_eye_corr, key=lambda item: item[0])[0]
    r_min_y = min(right_eye_corr, key=lambda item: item[1])[1]
    r_max_y = max(right_eye_corr, key=lambda item: item[1])[1]

    l_min_x = min(left_eye_corr, key=lambda item: item[0])[0]
    l_max_x = max(left_eye_corr, key=lambda item: item[0])[0]
    l_min_y = min(left_eye_corr, key=lambda item: item[1])[1]
    l_max_y = max(left_eye_corr, key=lambda item: item[1])[1]

    cropped_right = eyes[r_min_y:r_max_y, r_min_x:r_max_x]
    cropped_left = eyes[l_min_y:l_max_y, l_min_x:l_max_x]

    return cropped_right, cropped_left

def pos_estimation(cropped_eye):
    h, w = cropped_eye.shape

    gaussian_blur = cv2.GaussianBlur(cropped_eye, (9, 9), 0)
    median_blur = cv2.medianBlur(gaussian_blur, 3)

    thres_eye = cv2.adaptiveThreshold(median_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 33, 0)

    piece = int(w / 3)

    right_piece = thres_eye[0:h, 0:piece]
    center_piece = thres_eye[0:h, piece:piece + piece]
    left_piece = thres_eye[0:h, piece + piece:w]

    eye_pos, color = pixel_counter(right_piece, center_piece, left_piece)

    if np.sum(thres_eye == 0) > (0.8 * h * w):
        eye_pos = "CLOSED"
        color = [utils.RED, utils.BLACK]

    return eye_pos, color

def pixel_counter(first_piece, second_piece, third_piece):
    right_part = np.sum(first_piece == 0)
    center_part = np.sum(second_piece == 0)
    left_part = np.sum(third_piece == 0)

    eye_parts = [right_part, center_part, left_part]

    max_ind = eye_parts.index(max(eye_parts))

    if max_ind == 0 and (eye_parts[0] > eye_parts[1] + 10):
        pos_eye = "RIGHT"
        color = [utils.BLACK, utils.RED]
    elif max_ind == 2 and (eye_parts[2] > eye_parts[1] + 10):
        pos_eye = "LEFT"
        color = [utils.BLACK, utils.RED]
    else:
        pos_eye = "CENTER"
        color = [utils.BLACK, utils.GREEN]

    return pos_eye, color

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=.50, fy=.50, interpolation=cv2.INTER_CUBIC)

        r_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        res = face_mesh.process(r_frame)

        if res.multi_face_landmarks:
            mesh_coor = landmark_detect(frame, res, False)

            right_corr = [mesh_coor[p] for p in RIGHT_EYE]
            left_corr = [mesh_coor[p] for p in LEFT_EYE]

            crop_right, crop_left = eyes_extractor(frame, right_corr, left_corr)

            cv2.imshow('Right Eye', crop_right)
            cv2.imshow('Left Eye', crop_left)

            eye_pos, color = pos_estimation(crop_right)
            cv2.putText(frame, "Real-Time Eye Tracking and Eye Position Estimation ", (57, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            if eye_pos == "CENTER":
                utils.colorBackgroundText(frame, "CENTER", cv2.FONT_HERSHEY_COMPLEX, 1.3, (385, 100), 2, color[0],
                                          color[1], 10, 10)
            elif eye_pos == "LEFT":
                utils.colorBackgroundText(frame, "LEFT", cv2.FONT_HERSHEY_COMPLEX, 1.3, (200, 100), 2, color[0],
                                          color[1], 10, 10)
            elif eye_pos == "RIGHT":
                utils.colorBackgroundText(frame, "RIGHT", cv2.FONT_HERSHEY_COMPLEX, 1.3, (600, 100), 2, color[0],
                                          color[1], 10, 10)

        cv2.imshow("Image", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
