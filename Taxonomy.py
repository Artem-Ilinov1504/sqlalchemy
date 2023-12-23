from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///C:/Users/Ilinov/PycharmProjects/pythonProject20/data.db', echo=True)

Base = declarative_base()


class Zhivoe(Base):
    __tablename__ = "zhivoe"

    id = Column(Integer, primary_key=True)
    tsarstvo = Column(String)
    otdel = Column(String)
    clas = Column(String)
    poryadok = Column(String)
    semeystvo = Column(String)
    rod = Column(String)
    vid = Column(String)

    def __repr__(self):
        return f"<(Царство:{self.tsarstvo},Отдел:{self.otdel},Класс:{self.clas},Порядок:{self.poryadok}," \
               f"Семейство:{self.semeystvo}," \
               f"Род:{self.rod},Вид:{self.vid}')>"


Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)

session = Session()

zhivoe1 = Zhivoe(tsarstvo="Растения", otdel="Цветковые",clas="Двудольные",poryadok="Розоцветные",
                 semeystvo="Розовые",rod="Роза",vid="Роза обыкновенная")

zhivoe2 = Zhivoe(tsarstvo="Грибы", otdel="Базидиомикота",clas="Агарикомицеты",poryadok="Агариковые",
                 semeystvo="Аманитовые",rod="Мухомор",vid="Мухомор красный")

zhivoe3 = Zhivoe(tsarstvo="Бактерии", otdel="Протеобактерии",clas="Гамма-протеобактерии",poryadok="Enterobacteriales",
                 semeystvo="Enterobacteriaceae",rod="Escherichia",vid="Кишечная палочка")

zhivoe4 = Zhivoe(tsarstvo="Животные", otdel="Хордовые",clas="Млекопитающие",poryadok="Зайцеобразные",
                 semeystvo="Зайцевые",rod="Зайцы",vid="Заяц беляк")

session.add(zhivoe1)
session.add(zhivoe2)
session.add(zhivoe3)
session.add(zhivoe4)

session.commit()

zhivoe = session.query(Zhivoe).all()
for zhivoe in zhivoe:
    print(zhivoe)
