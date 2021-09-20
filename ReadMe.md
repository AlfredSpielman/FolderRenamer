# Folder Renamer
###version 1.0

Super simple code I used out of personal need. I have directory with hundreds of subfolders out of which many had dates
as names. But dates were in a wrong format - mostly "D.MM.YYYY" which everyone will agree was not a good idea. The best
format is ISO format: "YYYY-MM-DD". Oldest folders are dated back to 2008, the time when I didn't knew how bad this idea
was. Because of my stubbornness, I kept with once given format for many years, resulting with hundreds of ugly folder
names.

Finally, the time has come. I didn't wanted to do it manually, therefore here's the code. Take it, use it, adjust it and
remember - **the only correct date format is ISO format**.

Cheers!

---
If you want to adjust the code for your need, start with `line 26` where I've hardcoded date formats:
```python
patterns = [
        '%d.%m.%Y',  # DD.MM.YYYY
        '%Y.%m.%d'   # YYYY.MM.DD
    ]
```