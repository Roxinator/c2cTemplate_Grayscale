from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

# @app.route('/puppy_image', methods=['POST'])
# def puppy_image():
#     disability = request.form.get('input_disability', ' ')
#     dropdown = request.form.get('input_dropdown', ' ')
#     select = request.form.get('input_select', ' ')
#     freeform = request.form.get('input_freeform', ' ')
#     return render_template("index.html", input_data=dropdown,
#                             output="Enter your disability %s." %disability)
