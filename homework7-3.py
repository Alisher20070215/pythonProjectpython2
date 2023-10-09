import requests
from parcel import Selector

url = "https://cars.kg/offers/"

def get_html():
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    file = requests.get(
        "https://im.mashina.kg/tachka/images//b/5/2/b52bc189feda2d28fd9004b3462c2b57_640x480.jpg"
    )
    with open("test.jpg", "wb") as f:
        for chunk in file.iter_content(1024):
            f.write(chunk)

def parse_html(html):
    selector = Selector(text=html)
    return selector


if __name__ == "__main__":
    html = get_html()
    selector = parse_html(html)
    site_title = selector.css("title::text").get()
    cars = selector.css(".catalog-list-item")
    for c in cars:
        title = c.css(".catalog-item-caption::text").get().strip().replace("\n", "")
        print(title)
        car_url = f"{MAIN_URL}{c.attrib['href']}"
        print(car_url)
