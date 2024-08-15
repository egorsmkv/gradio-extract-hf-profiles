from pathlib import Path
from bs4 import BeautifulSoup


test = Path('test.html')

soup = BeautifulSoup(test.read_text(), features="html.parser")

links = []

for item in soup.find_all('a'):
    div_class = ' '.join(item.get('class'))
    if div_class == 'flex items-center gap-2':
        links.append(item)

profiles = {}
for link in links:
    hf_url = f'https://huggingface.co{link["href"]}'
    profile_name = link.text.replace('· ', '').strip()

    profiles[profile_name] = hf_url

for profile_name, hf_url in profiles.items():
    print(profile_name, hf_url)

print('---')

print(len(profiles.items()))
