# TEXT RECOGNITION USING OPENCV 

## A. PROJECT SUMMARY

**Project Title:** Text detection using OpenCV

**Team Members:** 
- Ahmad Hazim Bin Ahmad Rizal
- Mohamad Adam Danieal Bin Sluhudin Hamdan
- Adhwa Danish Bin Mohamad Noor
- Ahmad Nabil Bin Zulkifli


**Objectives:**
- To detect texts depicted in the image of the camera.
- To be able to convert the texts in the image into string.
- To enable users to copy and paste long texts detected in the image.

##  B. ABSTRACT 

This AI is created for the purpose of helping students with their research in their respective subjects. Be that as it may, but there are some materials (in forms of PDF) that
only has images in them. The texts and pages are all uploaded in images in the PDF which makes it hard for students to cite the materials into their written assignment as a
supporting answer. With this AI, the images in the PDF that has texts can be detected and converted into string. That way, the texts in the image, which weren't copiable then,
can now be copied into their written assignment. Problem solved.

Blind people rely on other senses apart from their sight senses. Having said that, they can't read texts from books or any other information pieces. However, nowadays we have a text-to-speech voice technology that detects string-type characters and converts it into a voice. It would be as if someone is reading you a book. With the 'Text Detection' AI, all we have to do is capture an image of the book's page and have it convert it into string. The string characters we obtained can be copied into the text-to-speech voice technology.



![AI](https://user-images.githubusercontent.com/80871331/115047295-f727c480-9f0a-11eb-9653-fb2551455435.PNG)
Figure 1 shows the AI system of Text detecting that change image text to String.


## C.  IMPLEMENTATION

#1. cv2.imread
This method returns an image that is loaded from the specified file.From our ptoject we need to upload an image file that contains words so the program could detect it.

![Code1](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/code1.png)

![Code2](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/code2.png)

#2. pytesseract.image_to_string(image)
this method is used to convert image into string. To store or transfer an Image to some we need to convert it into a string such that the string should portray the image which we give as input.

![Figure 2](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/pytess.png)

#3. cv2.imshow()
method is used to display an image in a window. The window automatically fits to the image size. In our project we have created a GUI to be interacted using tkinter. therefore we used this method to display the image in a window so that it shows the program is detecting the alphabets in the uploaded image.

![Figure 3](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/imshow.png)

#4 cv2.rectangle()
method is used to draw a rectangle on any image. In our peoject we already used cv2.imshow() to display the uploaded image, and to further show that the program is identifying alphabets that are currently in the image we used cv2.rectangle so that the program can use it to highlight the alphabets.

![Figure 4](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/rect.png)

#5. cv2.cvtColor() 
method is used to convert an image from one color space to another.in our project we use this function to help the program to identify the color of the image since this library is designed to solve computer vision problems.


## D.   PROJECT STRUCTURE

The following directory is our structure of our project:

- ├── dataset
- ├── examples
- │   ├── example_01.png
- │   └── example_02.png
- ├── Text_detector
- │   ├── pytesseract.image_to_string(img)
- │   └── pytesseract.image_to_boxes(img)
- ├── detect_character_image.py
- ├── Character_detector.model


The dataset/ directory contains the data described in the “Text Recognition ” section.

The two image examples/ are provided so that you can test the image that to be convetred to string to allow you to copy those word from an image..


## E.  RESULT AND CONCLUSION

Detecting the text using Text Detection OpenCV

Text Detection will detect the every part of the word in the input images, it will then display the text contain in the images. USer also will be able
to copy the display text into the computer

![Figure 5](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/sampletest.png)

In Figure 5 : detecting the input images, as we can see that it detects correctly and precise as long as the word is not crooked.

![Figure 6](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/sample.png)

In Figure 6 : The figure 5 shows the display of the text able to detect in the selected images.

As for conlcusion, the text detection is able to correctly detect the word in that selected images as long as the input text in the image is not crooked. We can say 
that the text detection system is 80% accurate to detect the text in the input images.


## F.   PROJECT PRESENTATION 

In this project, we learned how to create a Text Recognition AI program using OpenCV

We also used Tesseract optical character recognition(OCR) to detect any characters in the image.

The program specializes in detecting characters in images and enable them to be copied and pasted since the sentences inside the image has been converted into string and can, therefore be manipulated 

Our simple program also includes a small user interface for the user to insert the image into the program.

[![demo](https://github.com/hazimrizal/Artificial-Intelligence-Project/blob/main/images/ai%20textrecog.png)](https://www.youtube.com/watch?v=wuXnI7gNvPA "demo")



