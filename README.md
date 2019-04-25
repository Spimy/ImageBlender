# ImageBlender
A simple Python program that merges two pictures together like the app "Layout" does. Made this to ease my life since I don't want to manually merge all my images manually using "Layout" so this program does it all for me at the click of a button in a specific directory. It also adds a watermark of your Instagram tag.

### **Setup**
- Install Python3: https://www.python.org/
- Install PIL: `pip3 install pillow`
- Put the `main.py` file in the folder with the pictures you want to merge
- Assign the `name` variable with your Instagram tag instead of mine (open file using text editor like Notepad++ or Sublime Text. Do NOT open the file using Notepad as it may mess up the indentation)
- Run `main.py` and done

### **Images**
The images you want to merge must be in proper order.
Example: image1.png, image2.png, image3.png, image4.png...
When merging, it will merge image1.png and image2.png together and image3.png and image4.png together
So make sure you have them in the order you want the to merge
Make sure you don't have unneeded images in the same folder.
PLEASE NOTE THAT THIS ONLY MERGE **TWO** IMAGES!

### **Output**
All images merged will be output into a folder called `output` in the same directory as your images.
This folder can be created manually or if you didn't, the program will do so for you.
Once the images are full merged, the console will output `Done`. Simply hit Enter and now, post your newly merged pictures on Instagram with your very own watermark as well!
