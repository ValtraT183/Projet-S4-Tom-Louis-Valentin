from PIL import Image, ImageTk 



def recup_image(numero):
            img = Image.open(f"Image/face{numero}.png")
            img = img.resize((75,75))
            return ImageTk.PhotoImage(img)

 

def recup_gain(mise,tot_a,tot) :
        if tot_a > tot :
                return 0
        elif tot_a == tot :
                return mise/2
        else :
                return mise*2
        