import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

choice = input('Pic or vid?: ')
choice = choice.upper()
while choice not in ['PIC', 'VID']:
    print(choice, ' is not an option!')
    choice = input('Please type in "pic" or "vid" only: ').upper()

if choice == 'VID':

    cap = cv.VideoCapture('cv_vids/1145675382794154.mp4')
    frame = cap.read()

    show_size = True
    while True:
        isTrue, frame = cap.read()

        #prevents error when frame is None at the last frame of video
        if frame is None:
            break
        frame = rescaleFrame(frame, 0.5)
        cv.imshow('untitled', frame)

        #shows size of video
        if show_size:
            print('Video size: ', frame.shape)
            show_size = False

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

elif choice == 'PIC':
    img = cv.imread('cv_pics/cat2.jpg')
    cv.imshow('Look at this oversized cat!', img)
    print(img)
    cv.waitKey(0)


