# multicracker
Simple tool for pentest devices with default credentials and taking PoC of vulnerability
## Installation
``` bash
git clone https://github/stderr2d0ma1n/multicracker
cd multicracker
pip3 install selenium
```
## Usage
``` bash
python3 multicracker.py -l tomsmith -p SuperSecretPassword! -xl '//*[@id="username"]' -xp '//*[@id="password"]' -xb '/html/body/div[2]/div/div/form/button' -ul test_url_list.txt
```
