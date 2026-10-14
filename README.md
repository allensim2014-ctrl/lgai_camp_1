# Re:Step UI Pilot

Re:Step is a Streamlit UI pilot for a photo-based, step-by-step recycling guide.
The current screen supports image upload and six selectable waste categories,
then displays a three-step example guide for the selected category.

Image detection is not connected in this pilot. The UI labels the guide as an
example and does not claim to have analyzed the uploaded image.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
