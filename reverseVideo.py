import cv2

cap = cv2.VideoCapture('Neo.mkv')

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out =  cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width),int(height)))

frame_index  = frames-1

if(cap.isOpened()):
    while(frame_index != 0):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame = cap.read()

        out.write(frame)
        frame_index = frame_index-1

        if(frame_index%100 == 0):
            print(frame_index)

out.release()
cap.release()
cv2.destroyAllWindows()