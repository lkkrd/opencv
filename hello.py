import cv2 as cv

choice = input('Pic or vid?: ')
choice = choice.upper()
while choice not in ['PIC', 'VID']:
    print(choice, ' is not an option!')
    choice = input('Please type in "pic" or "vid" only: ').upper()

if choice == 'VID':

    cap = cv.VideoCapture('cv_vids/1145675382794154.mp4')
    while True:
        isTrue, frame = cap.read()
        cv.imshow('untitled', frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

elif choice == 'PIC':
    img = cv.imread('cv_pics/cat2.jpg')
    cv.imshow('Look at this oversized cat!', img)
    cv.waitKey(0)


