from app import app, init_database

if __name__ == '__main__':
    init_database(app)
    app.run()
