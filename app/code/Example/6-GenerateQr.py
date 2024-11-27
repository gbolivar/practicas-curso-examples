import qrcode

# Generar un código QR para un sitio legítimo
data = "https://bancodevenezuela.com/"
qr = qrcode.make(data)

# Guardar el código QR en un archivo
qr.save("codigo_qr_legitimo.png")

print("Código QR generado de forma segura.")