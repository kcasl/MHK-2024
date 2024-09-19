from PIL import Image
from captcha.image import ImageCaptcha
from io import BytesIO
import random
import os


def generate_captcha(text: str) -> Image:
    captcha = ImageCaptcha(
        width=256,
        height=256,
        fonts=['Helvetica', 'Arial', 'Times New Roman', 'Courier', 'Menlo', 'Verdana'],
        font_sizes=(90, 100, 120)
    )
    data: BytesIO = captcha.generate(text)
    image: Image = Image.open(data)
    return image


def main() -> None:

    # 폴더에 집어 넣자
    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)

    # 원하는 만큼 captcha 만들고 폴더에 넣기
    for _ in range(500):
        random_numbers = random.sample(range(10), 6)
        random_numbers_string = ''.join(map(str, random_numbers))
        image = generate_captcha(random_numbers_string)

        # 이미지 파일 이름은 각자 숫자로 설정
        image.save(os.path.join(output_dir, f'{random_numbers_string}.png'))

    print(f'All CAPTCHA images have been saved to the folder "{output_dir}".')


if __name__ == '__main__':
    main()
