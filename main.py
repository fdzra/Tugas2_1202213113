from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import datetime;

app = Flask(__name__)

# Mysql Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_api'


mysql = MySQL(app)

# ======================================================================================
# START BARANG
# ======================================================================================
@app.route('/barang')
def index_barang():
    where = ''
    nama_barang = request.args.get('nama_barang')
    if nama_barang != None:
        where += " and barang.nama_barang like '%" + nama_barang + "%' "
        
    cursor = mysql.connection.cursor()
    cursor.execute('select * from barang where true ' + where)
    
    column_names = [i[0] for i in cursor.description]
    
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
            'data': data
        }
    return jsonify(data)

@app.route('/barang/<id>')
def detail_barang(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from barang where id = '" + id + "' limit 1")
    
    column_names = [i[0] for i in cursor.description]
    
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))
    
    if (len(data) == 0):
        return jsonify({
            'message': 'ID tidak ditemukan',
            'code': 403,
            'timestamp': datetime.datetime.now(),
        })
        
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
            'data': data[0]
        }
    return jsonify(res)

@app.route('/barang/add', methods=['POST'])
def add_barang():
    nama_barang = request.json.get('nama_barang')
    harga = request.json.get('harga')
    stok = request.json.get('stok')
    if nama_barang == None or harga == None or stok == None: 
        return jsonify({
            'message': 'Periksa input anda',
            'code': 400,
            'timestamp': datetime.datetime.now(),
        }), 400
        
    val = (nama_barang, harga, stok)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO `barang` (`nama_barang`, `harga`, `stok`) VALUES (%s, %s, %s)''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 201,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 201

@app.route('/barang/update/<id>', methods=['PUT'])
def update_barang(id):
    nama_barang = request.json.get('nama_barang')
    harga = request.json.get('harga')
    stok = request.json.get('stok')
    if nama_barang == None or harga == None or stok == None: 
        return jsonify({
            'message': 'Periksa input anda',
            'code': 400,
            'timestamp': datetime.datetime.now(),
        }), 400
        
    val = (nama_barang, harga, stok, id)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''UPDATE `barang` SET `nama_barang` = %s, `harga` = %s, `stok` = %s WHERE `barang`.`id` = %s''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 200

@app.route('/barang/delete/<id>', methods=['DELETE'])
def delete_barang(id):
    val = (id)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE from barang WHERE `barang`.`id` = %s''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 200
# ======================================================================================
# END BARANG
# ======================================================================================

# ======================================================================================
# START PELANGGAN
# ======================================================================================
@app.route('/pelanggan')
def index_pelanggan():
    where = ''
    nama_pelanggan = request.args.get('nama_pelanggan')
    if nama_pelanggan != None:
        where += " and pelanggan.nama_pelanggan like '%" + nama_pelanggan + "%' "
        
    telepon = request.args.get('telepon')
    if telepon != None:
        where += " and pelanggan.telepon = '" + telepon + "' "
    
    alamat = request.args.get('alamat')
    if alamat != None:
        where += " and pelanggan.alamat like '%" + alamat + "%' "
        
    cursor = mysql.connection.cursor()
    cursor.execute('select * from pelanggan where true ' + where)
    
    column_names = [i[0] for i in cursor.description]
    
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
            'data': data
        }
    return jsonify(res)

@app.route('/pelanggan/<id>')
def detail_pelanggan(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from pelanggan where id = '" + id + "' limit 1")
    
    column_names = [i[0] for i in cursor.description]
    
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))
    
    if (len(data) == 0):
        return jsonify({
            'message': 'ID tidak ditemukan',
            'code': 403,
            'timestamp': datetime.datetime.now(),
        })
        
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
            'data': data[0]
        }
    return jsonify(res)

@app.route('/pelanggan/add', methods=['POST'])
def add_pelanggan():
    nama_pelanggan = request.json.get('nama_pelanggan')
    alamat = request.json.get('alamat')
    telepon = request.json.get('telepon')
    if nama_pelanggan == None or alamat == None or telepon == None: 
        return jsonify({
            'message': 'Periksa input anda',
            'code': 400,
            'timestamp': datetime.datetime.now(),
        }), 400
        
    val = (nama_pelanggan, alamat, telepon)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO `pelanggan` (`nama_pelanggan`, `alamat`, `telepon`) VALUES (%s, %s, %s)''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 201,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 201

@app.route('/pelanggan/update/<id>', methods=['PUT'])
def update_pelanggan(id):
    nama_pelanggan = request.json.get('nama_pelanggan')
    alamat = request.json.get('alamat')
    telepon = request.json.get('telepon')
    if nama_pelanggan == None or alamat == None or telepon == None: 
        return jsonify({
            'message': 'Periksa input anda',
            'code': 400,
            'timestamp': datetime.datetime.now(),
        }), 400
        
    val = (nama_pelanggan, alamat, telepon, id)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''UPDATE `pelanggan` SET `nama_pelanggan` = %s, `alamat` = %s, `telepon` = %s WHERE `pelanggan`.`id` = %s''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 200

@app.route('/pelanggan/delete/<id>', methods=['DELETE'])
def delete_pelanggan(id):
    val = (id)
    
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE from pelanggan WHERE `pelanggan`.`id` = %s''', val)
    
    cursor.connection.commit()
    
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 200
# ======================================================================================
# END PELANGGAN
# ======================================================================================

# ======================================================================================
# START PENJUALAN
# ======================================================================================
@app.route('/penjualan')
def index_penjualan():
    where = ''
    nama_pelanggan = request.args.get('nama_pelanggan')
    if nama_pelanggan != None:
        where += " and pelanggan.nama_pelanggan like '%" + nama_pelanggan + "%' "
        
    telepon = request.args.get('telepon')
    if telepon != None:
        where += " and pelanggan.telepon = '" + telepon + "' "
    
    alamat = request.args.get('alamat')
    if alamat != None:
        where += " and pelanggan.alamat like '%" + alamat + "%' "
        
    cursor = mysql.connection.cursor()
    cursor.execute('select penjualan.id, tanggal, nama_pelanggan, alamat, telepon, total from penjualan join pelanggan on pelanggan.id = penjualan.id_pelanggan where true ' + where)
    
    column_names = [i[0] for i in cursor.description]
    
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))
    
    for item in data:
        cursor.execute("select barang.nama_barang, jumlah, harga as harga_satuan, subtotal from detail_penjualan join barang on barang.id = detail_penjualan.id_barang where id_penjualan = '" + str(item['id']) + "'")
        cn = [i[0] for i in cursor.description]
        child = []
        for itt in cursor.fetchall():
            child.append(dict(zip(cn, itt)))
        item['detail'] = child
        
    res = {
            'message': 'Berhasil',
            'code': 200,
            'timestamp': datetime.datetime.now(),
            'data': data
        }
    return jsonify(res)

@app.route('/penjualan/transaksi', methods=['POST'])
def transaksi_penjualan():
    cursor = mysql.connection.cursor()
    
    tanggal = request.json.get('tanggal')
    id_pelanggan = request.json.get('id_pelanggan')
    detail = request.json.get('detail')
    
    # Penjualan
    val = (tanggal, id_pelanggan)
    cursor.execute('''INSERT INTO `penjualan` (`tanggal`, `id_pelanggan`) VALUES (%s, %s)''', val)
    # cursor.connection.commit()
    id_penjualan = mysql.connection.insert_id()
    
    # Detail Penjualan
    total = 0
    for item in detail:
        id_barang = item['id_barang']
        jumlah = item['jumlah']
        
        cursor.execute("select * from barang where id = '" + str(id_barang) + "' limit 1")
        barang = cursor.fetchone()
        if barang == None:
            return jsonify({
                'message': 'ID Barang tidak ditemukan',
                'code': 403,
                'timestamp': datetime.datetime.now(),
            })
            
        subtotal = barang[2] * jumlah
        total = total + subtotal
        detail_val = (id_penjualan, id_barang, jumlah, subtotal)
        cursor.execute('''INSERT INTO `detail_penjualan` (`id_penjualan`, `id_barang`, `jumlah`, `subtotal`) VALUES (%s, %s, %s, %s)''', detail_val)
        
    valEditPenjualan = (total, id_penjualan)
    cursor.execute('''UPDATE `penjualan` SET `total` = %s WHERE `penjualan`.`id` = %s''', valEditPenjualan)
    cursor.connection.commit()
    res = {
            'message': 'Transaksi Berhasil',
            'code': 201,
            'timestamp': datetime.datetime.now(),
        }
    return jsonify(res), 201

# ======================================================================================
# START PENJUALAN
# ======================================================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)