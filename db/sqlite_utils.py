import sqlite3
from models.item_dto import ItemDTO

def create_database(db_path: str = "data/items.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier TEXT,
            articleCode TEXT,
            supplierCode TEXT,
            description TEXT,
            price REAL DEFAULT 0,
            netto REAL DEFAULT 0,
            ivato REAL DEFAULT 0,
            quantity INTEGER,
            ean TEXT,
            UNIQUE(supplier, articleCode)  -- deduplication
        )
    ''')
    conn.commit()
    conn.close()
    print(f"✅ SQLite DB initialized at: {db_path}")

def insert_items(items: list[ItemDTO], db_path: str = "data/items.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    values = [
        (item.supplier, item.articleCode, item.supplierCode, item.description, item.price,item.netto, item.ivato, item.quantity, item.ean)
        for item in items
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO items 
        (supplier, articleCode, supplierCode, description, price, netto, ivato, quantity, ean)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', values)

    conn.commit()
    conn.close()
    print(f"✅ Inserted {len(items)} items into {db_path}")

def search_items_by_name(query: str, db_path: str = "data/items.db") -> list[ItemDTO]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT supplier, articleCode, supplierCode, description, price, quantity, ean, netto, ivato
        FROM items
        WHERE articleCode LIKE ? OR description LIKE ?
        ORDER BY price ASC
    ''', (f'%{query}%', f'%{query}%'))

    rows = cursor.fetchall()
    conn.close()

    return [ItemDTO(*row) for row in rows]
