from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)
bot = instaloader.Instaloader()

@app.route('/get_info')
def get_info():
    username = request.args.get('username')
    profile = instaloader.Profile.from_username(bot.context, username)

    data = {
        'username': profile.username,
        'userid': profile.userid,
        'mediacount': profile.mediacount,
        'followers': profile.followers,
        'followees': profile.followees,
        'biography': profile.biography
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()
