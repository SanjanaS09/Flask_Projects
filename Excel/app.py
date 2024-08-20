from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.get('/')
def upload():
    return render_template('index.html')

@app.post('/view')
def view():
    file = request.files.get('file')

    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
        return 'Invalid file type'

    file.save(file)
    df = pd.read_excel(file)
    
    selected_columns = ['First Name', 'Last Name', 'Gender']  
    if not set(selected_columns).issubset(df.columns):
        return "Some columns are not found in the uploaded file"

    extracted_df = df[selected_columns]
    
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine = 'openpyxl') as writer:
        extracted_df.to_excel(writer, index=False, sheet_name='SelectedData')
    writer.save()
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="extracted_data.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    app.run(debug=True)
