import streamlit as st
import qrcode
import io

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)

def get_QR_image(msg):
    qr.add_data(input_str)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = io.BytesIO()
    qr_img.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

st.set_page_config(
    page_title="QRコード生成"
)

st.markdown('# QRコード生成')
st.text("QRコードに変換する文字列を入力してください")
input_str=st.text_input('文字列の入力',placeholder='https://aaaa.com/')

st.text(f'入力結果 "{input_str}"')

if st.button("QRコード生成"):
    if input_str:
        qr_img = get_QR_image(input_str)
        
        st.download_button(
            label="画像ダウンロード",
            data=qr_img,
            file_name="generated_qr.png",
            mime='image/png'
        )
        st.image(qr_img)
    else:
        st.error("QRコードに変換する文字列が空です")

