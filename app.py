import os
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from supabase import create_client, Client

app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.route('/', methods=['GET'])
def get_data():
    return render_template("index.html")


@app.route('/submit', methods=["POST"])
def submit():
    form = request.form

    gt_nam_bac = int(form["gt_nam_bac"])
    gen_nam_bac = int(form["gen_nam_bac"])
    ex_nam_bac = int(form["ex_nam_bac"])

    gt_nam_nam = int(form["gt_nam_nam"])
    gen_nam_nam = int(form["gen_nam_nam"])
    ex_nam_nam = int(form["ex_nam_nam"])

    gt_nu_bac = int(form["gt_nu_bac"])
    gen_nu_bac = int(form["gen_nu_bac"])
    ex_nu_bac = int(form["ex_nu_bac"])

    gt_nu_nam = int(form["gt_nu_nam"])
    gen_nu_nam = int(form["gen_nu_nam"])
    ex_nu_nam = int(form["ex_nu_nam"])

    gt_nu_trung = int(form["gt_nu_trung"])
    gen_nu_trung = int(form["gen_nu_trung"])
    ex_nu_trung = int(form["ex_nu_trung"])

    data = supabase.table('score') \
                        .insert({"nam-bac-gt": gt_nam_bac, "nam-bac-gen": gen_nam_bac, "nam-bac-ex": ex_nam_bac,
                                 "nam-nam-gt": gt_nam_nam, "nam-nam-gen": gen_nam_nam, "nam-nam-ex": ex_nam_nam,
                                 "nu-bac-gt": gt_nu_bac, "nu-bac-gen": gen_nu_bac, "nu-bac-ex": ex_nu_bac,
                                 "nu-nam-gt": gt_nu_nam, "nu-nam-gen": gen_nu_nam, "nu-nam-ex": ex_nu_nam,
                                 "nu-trung-gt": gt_nu_trung, "nu-trung-gen": gen_nu_trung, "nu-trung-ex": ex_nu_trung}) \
                        .execute()
    
    return render_template("after.html")


if __name__ == '__main__':
    app.run(port=12000)