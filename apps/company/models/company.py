from apps.commons.database import TimestampMixin
from apps.extensions import db


class Company(db.Model, TimestampMixin):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)

    names = db.relationship('CompanyName',
                            backref='companies', lazy='joined')

    tags = db.relationship('CompanyTag',
                           backref='companies', lazy='joined')


class CompanyName(db.Model, TimestampMixin):
    __tablename__ = 'company_names'
    __table_args__ = (
        db.UniqueConstraint('company_id', 'lang'),
    )

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    lang = db.Column(db.String(2), nullable=False)


class Tag(db.Model, TimestampMixin):
    __tablename__ = 'tags'
    __table_args__ = (
        db.UniqueConstraint('tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), nullable=False)
    lang = db.Column(db.String(2), nullable=False)


class CompanyTag(db.Model, TimestampMixin):
    __tablename__ = 'company_tags'
    __table_args__ = (
        db.UniqueConstraint('company_id', 'tag_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    tag = db.relationship(Tag, lazy='joined')


class SearchCompany(db.Model, TimestampMixin):
    __tablename__ = 'search_companies'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    initial_index = db.Column(db.String(255), nullable=False)
    phoneme_index = db.Column(db.String(255), nullable=False)
