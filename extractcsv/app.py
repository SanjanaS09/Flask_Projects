from flask import Flask, request, render_template, send_file, Response
import pandas as pd
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        uploaded_file = request.files.get('csvfile')
        if not uploaded_file or not uploaded_file.filename.endswith('.csv'):
            return 'Invalid file type'

        df = pd.read_csv(uploaded_file)

        selected_columns = ['First Name', 'Last Name', 'Email']
        if not set(selected_columns).issubset(df.columns):
            return "Some columns are not found in the uploaded file"

        return render_template('data.html', columns=df.columns.tolist(), filename='uploaded_file')

    return render_template('data.html')

@app.route('/download', methods=['POST'])
def download():
    selected_columns = request.form.getlist('columns')

    df = pd.read_csv(io.StringIO(request.form['csv_data']))

    filtered_df = df[selected_columns]

    output = io.StringIO()
    filtered_df.to_csv(output, index=False)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="extracted_data.csv", mimetype='csv')

if __name__ == '__main__':
    app.run(debug=True)
