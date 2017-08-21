# 
class Sity():
    def __init__(self):
        self.list = []
        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        cur.execute('SELECT * FROM Sities_list')
        for i in cur.fetchall():
            self.list.append(i)
        return list

    def

def main():


if __name__ == '__main__':
    main()