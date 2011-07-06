import quickwork



class TestSimple(object):

    def test_make_table(self):

        database = quickwork.Database()

        database.create_table("fred", {"name" : 20,
                                       "date" : "date",
                                       "bool" : "bool",
                                       "int"  : "int",
                                       "decimal" : "decimal"}
                               )

        metadata = database.metadata

        assert "fred" in database.tables
        assert "fred" in metadata.tables

        select_all = database.tables["fred"].select().execute()
        assert select_all.fetchone() == None


    def test_insert_data(self):

        database = quickwork.Database()
        database.create_table("fred", {"name" : 20,
                                       "info": 30}
                             )
        info = database.insert_well_formed_data([
            dict(name = u"fred", info = u"moo"),
            dict(name = u"fred2", info = u"moo2"),
            dict(name = u"fred3", info = u"moo3"),
            dict(name = u"fred4", info = u"moo4"),
        ])

        table = database.tables["fred"]

        assert info.rowcount == 4, info.rowcount

        select_all = table.select().execute().fetchall()

        assert len(select_all) == 4

        count_all = table.select().count().execute().fetchall()[0][0]
        assert count_all == 4, count_all


    def test_load_from_string(self):

        database = quickwork.Database()

        text = """a,b,c
fdsfsad,"fdsa\n\tf
sa",23
fafsd,fdsafasd,21"""

        database.load_csv(name = "fred", buffer = text)

        assert "fred" in database.tables
        assert "fred" in database.metadata.tables

        select_all = database.tables["fred"].select().execute().fetchall()
        assert len(select_all) == 2

    def test_load_unicode_from_file(self):

        database = quickwork.Database()
        database.load_csv("wee.txt", format = {"delimiter" : ","})

        assert "wee" in database.tables
        assert "wee" in database.metadata.tables

        select_all = database.tables["wee"].select().execute().fetchall()
        print select_all
        assert len(select_all) == 3

