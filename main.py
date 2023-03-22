from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True) # esli etoj linii netu to run ne s rabotaet
    