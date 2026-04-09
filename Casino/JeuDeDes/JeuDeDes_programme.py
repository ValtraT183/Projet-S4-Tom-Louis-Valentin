from PIL import Image, ImageTk 







# Fonction ouvrir image (et conversion)
# -------------------------------------------------------------------------------------------

def recup_image(numero):
            img = Image.open(f"Image/face{numero}.png")
            img = img.resize((75,75))
            return ImageTk.PhotoImage(img)

# -------------------------------------------------------------------------------------------

 




# Fonction récuperer gain
# -------------------------------------------------------------------------------------------

def recup_gain(mise,tot_a,tot) :
        if tot_a > tot :
                return 0
        elif tot_a == tot :
                return round(mise/2)
        else:
                return round(mise*2)

# -------------------------------------------------------------------------------------------

        
