import qrcode
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data( '''BEGIN:VCARD
VERSION:3.0
N:KOUDOU;Christelle
FN:Christelle KOUDOU
TITLE:Agent commercial
ORG:Bernabé, Technibat, Yeshi Groupe
URL:www.bernabeafrique.com
EMAIL;TYPE=INTERNET:christelle.koudou@bernabeafrique.com
TEL;TYPE=voice,work,pref:+225 05 06 736 640
TEL;TYPE=voice,cell,pref:
TEL;TYPE=fax,work,pref:
ADR:;;Bd de Marseille, Km 4;Abidjan;;01 B.P. 1867 Abidjan 01;Côte d'Ivoire
END:VCARD ''')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('Christelle KOUDOU.png')