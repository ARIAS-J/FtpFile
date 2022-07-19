# FtpFile

### Setup

1. Create a virtual env
```bash
py -m venv venv
```

2. Activate virtual env
```bash
./venv/Scripts/activate
```
3. Install requirements
```bash
pip install -r requirements.txt
```

4. Create .env file based on .env.example

5. Edit file locations in main.py 
```python
# File Data
file_destination = '{TARGET FILE HERE}'
file_source = f'C:\\YOUR\\PATH\\HERE\\{file_destination}'
```

6. Run program
```bash
py main.py
```
