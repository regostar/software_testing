from flask import Flask, session, jsonify, request, render_template

app = Flask(__name__)
app.secret_key = "replace-with-your-own-secret"

# Enhanced weapon catalog with prices and better rarities
WEAPONS = [
    {
        "id": 1,
        "name": "Assault Rifle",
        "rarity": "Rare",
        "damage": 35,
        "fire_rate": 5.5,
        "price": 800,
        "image": "https://fortnite-api.com/images/cosmetics/br/bid_116_assassin/icon.png"
    },
    {
        "id": 2,
        "name": "Pump Shotgun",
        "rarity": "Epic",
        "damage": 80,
        "fire_rate": 1.0,
        "price": 1200,
        "image": "https://fortnite-api.com/images/cosmetics/br/eid_pumpernickel/icon.png"
    },
    {
        "id": 3,
        "name": "SCAR",
        "rarity": "Legendary",
        "damage": 42,
        "fire_rate": 5.5,
        "price": 1500,
        "image": "https://fortnite-api.com/images/cosmetics/br/cid_083_athena_commando_f_space/icon.png"
    },
    {
        "id": 4,
        "name": "SMG",
        "rarity": "Uncommon",
        "damage": 25,
        "fire_rate": 10,
        "price": 500,
        "image": "https://fortnite-api.com/images/cosmetics/br/eid_smorgasbord/icon.png"
    },
    {
        "id": 5,
        "name": "Burst Assault Rifle",
        "rarity": "Epic",
        "damage": 37,
        "fire_rate": 4.0,
        "price": 1200,
        "image": "https://fortnite-api.com/images/cosmetics/br/cid_a_272_athena_commando_f_skirmishpink/icon.png"
    },
    {
        "id": 6,
        "name": "Heavy Sniper Rifle",
        "rarity": "Legendary",
        "damage": 150,
        "fire_rate": 0.7,
        "price": 2000,
        "image": "https://fortnite-api.com/images/cosmetics/br/harvest_id_110_darkninja/icon.png"
    },
    {
        "id": 7,
        "name": "Tactical Shotgun",
        "rarity": "Uncommon",
        "damage": 72,
        "fire_rate": 1.5,
        "price": 600,
        "image": "https://fortnite-api.com/images/cosmetics/br/cid_258_athena_commando_m_robottrouble/icon.png"
    },
    {
        "id": 8,
        "name": "Rocket Launcher",
        "rarity": "Epic",
        "damage": 120,
        "fire_rate": 0.75,
        "price": 1800,
        "image": "https://fortnite-api.com/images/cosmetics/br/eid_rocket/icon.png"
    }
]

@app.before_request
def ensure_cart():
    session.setdefault("cart", [])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/weapons")
def list_weapons():
    return jsonify(WEAPONS)

@app.route("/api/cart", methods=["GET", "POST"])
def manage_cart():
    if request.method == "GET":
        # return full weapon objects in cart
        cart_ids = session["cart"]
        items = [w for w in WEAPONS if w["id"] in cart_ids]
        return jsonify(items)
    else:
        data = request.get_json() or {}
        wid = data.get("id")
        if not any(w["id"] == wid for w in WEAPONS):
            return jsonify({"error": "Weapon not found"}), 404
        session["cart"].append(wid)
        session.modified = True
        return jsonify({"message": "Added to cart"}), 201

@app.route("/api/cart/clear", methods=["POST"])
def clear_cart():
    session["cart"] = []
    session.modified = True
    return jsonify({"message": "Cart cleared"}), 200

@app.route("/api/cart/remove/<int:item_id>", methods=["POST"])
def remove_from_cart(item_id):
    if item_id in session["cart"]:
        session["cart"].remove(item_id)
        session.modified = True
        return jsonify({"message": "Item removed from cart"}), 200
    return jsonify({"error": "Item not in cart"}), 404

if __name__ == "__main__":
    app.run(debug=True) 