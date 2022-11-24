from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)
# пипяо starts here


@app.route("/")
def test():
    return render_template('mainq.html')


def main():
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
