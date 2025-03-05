from flask import Flask, request, jsonify
from voice_cloning import clone_voice

app = Flask(__name__)

@app.route('/clone-voice', methods=['POST'])
def clone_voice_endpoint():
    file = request.files['file']
    target_voice_model = request.form['target_voice_model']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)
    
    cloned_voice = clone_voice(file_path, target_voice_model)
    
    return jsonify({"cloned_voice": cloned_voice})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
