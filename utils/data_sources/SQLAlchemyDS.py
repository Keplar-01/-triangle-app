from database import Session
from utils.data_sources.IDataSource import IDataSource


class SQLAlchemyDataSource(IDataSource):
    def __init__(self, session: Session):
        self.session = session

    def get_list(self, table_type, *args, **kwargs):
        return self.session.query(table_type).all()

    def get_item(self, item_id, table_type, *args, **kwargs):
        return self.session.query(table_type).filter_by(id=item_id).first()

    def insert_item(self, item, *args, **kwargs):
        self.session.add(item)
        self.session.commit()

    def update_item(self, item, table_type, *args, **kwargs):
        self.session.commit()
