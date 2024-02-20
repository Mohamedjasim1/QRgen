from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import qrcode
import os
def index(request):

    if(request.method=="POST"):
        username=request.POST.get('username')
        clas=request.POST.get('class')
        dept=request.POST.get('dept')
        txt=f"NAME:{username} \n CLASS:{clas} \n DEPARTMENT:{dept}"

        print(txt)
      
        img=qrcode.make(txt)
        pathh=r"C:\Users\selva\OneDrive\Desktop\QRgen\qrcodeproject\qrcodegen\static\images\qr_img.png"
        img.save(r"C:\Users\selva\OneDrive\Desktop\QRgen\qrcodeproject\qrcodegen\static\images\qr_img.png")
        

        print(pathh)
        '''destination_path = os.path.join(folder_path, file_name)
    

        with open(file_path, 'rb') as source_file:
    
            with open(destination_path, 'wb') as destination_file:
       
                destination_file.write(source_file.read())'''

        
        
        
        return render(request,"qrcodegen/qrcode.html",{"qrimg":pathh})
    return render(request,"qrcodegen/sam.html")
    

