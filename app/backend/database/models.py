# import
from sqlalchemy import (
    Column, Identity, ForeignKey, func, Integer, String, DateTime, Boolean, Date, Float, DECIMAL,
    TIMESTAMP, LargeBinary, Time)
from sqlalchemy.orm import relationship

# local import
from app.backend.database.config import BASE


"""
Data models that mimics actual database tables for the session manager object define in config.py
"""

class Province(BASE):
    __tablename__ = "province"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=10, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys

    # relations
    cantons = relationship("Canton", back_populates="province", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "name": self.name, "log_date": self.log_date.isoformat() if self.log_date else None}


class Canton(BASE):
    __tablename__ = "canton"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=50, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys
    id_province = Column(Integer, ForeignKey("refer.province.id"), nullable=False)
    # relations
    province = relationship("Province", back_populates="cantons")
    districts = relationship("District", back_populates="canton", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "name": self.name, "id_province": self.id_province,
                "log_date": self.log_date.isoformat() if self.log_date else None}


class District(BASE):
    __tablename__ = "district"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=200, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys
    id_canton = Column(Integer, ForeignKey("refer.canton.id"), nullable=False)
    # relations
    canton = relationship("Canton", back_populates="districts")
    addresses = relationship("Address", back_populates="district", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "name": self.name, "id_canton": self.id_canton,
                "log_date": self.log_date.isoformat() if self.log_date else None}


class User(BASE):
    __tablename__ = "user"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, Identity(start=400, increment=1, cycle=False), primary_key=True)
    identification = Column(String(25), nullable=False, unique=True)
    name = Column(String(75), nullable=False)
    lastname = Column(String(75), nullable=False)
    lastname2 = Column(String(75), nullable=False)
    gender = Column(String(25), nullable=False)
    birthday = Column(Date, nullable=False)
    civil = Column(String(25), nullable=False)
    children = Column(Integer, nullable=False, server_default="0")
    password = Column(String(75), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(25), nullable=False, unique=True)
    gross_income = Column(DECIMAL(12, 8), nullable=False, server_default="0.00")
    status = Column(Boolean, nullable=False, server_default="False")
    create_date = Column(Date, nullable=False)
    update_date = Column(Date, nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign key

    # relationships
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    user_roles = relationship("User_Role", back_populates="user", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "identification": self.identification, "name": self.name, "lastname": self.lastname,
                "lastname2": self.lastname2, "gender": self.gender, "birthday": self.birthday, "civil": self.civil,
                "children": self.children, "password": self.password, "email": self.email, "phone": self.phone,
                "gross_income": self.gross_income, "status": self.status, "create_date": self.create_date,
                "update_date": self.update_date, "log_date": self.log_date.isoformat() if self.log_date else None}


class Address(BASE):
    __tablename__ = "address"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=300, increment=1, cycle=False), primary_key=True)
    details = Column(String(300), nullable=False)
    postal = Column(String(20), nullable=True)
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys
    id_district = Column(Integer, ForeignKey("refer.district.id"), nullable=False)
    id_user = Column(Integer, ForeignKey("auth.user.id"), nullable=False)
    # relations
    district = relationship("District", back_populates="addresses")
    user = relationship("User", back_populates="addresses")

    # dict class
    def to_dict(self):
        return {"id": self.id, "details": self.details, "postal": self.postal, "id_district": self.id_district,
                "id_user": self.id_user, "log_date": self.log_date.isoformat() if self.log_date else None}


class Department(BASE):
    __tablename__ = "department"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=50, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    create_date = Column(Date, nullable=False)
    update_date = Column(Date, nullable=False)
    # foreign keys

    # relations
    roles = relationship("Role", back_populates="department", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "name": self.name, "create_date": self.create_date, "update_date": self.update_date}


class Schedule(BASE):
    __tablename__ = "schedule"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=60, increment=1, cycle=False), primary_key=True)
    type = Column(String(75), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    hours = Column(Integer, nullable=False, server_default="0")
    # foreign keys

    # relations
    roles = relationship("Role", back_populates="schedule", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "type": self.type, "start_time": self.start_time, "end_time": self.end_time,
                "hours": self.hours}


class Role(BASE):
    __tablename__ = "role"
    __table_args__ = {"schema": "refer"}
    # rows
    id = Column(Integer, Identity(start=60, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    type = Column(String(75), nullable=False)
    create_date = Column(Date, nullable=False)
    update_date = Column(Date, nullable=False)
    status = Column(Boolean, nullable=False, server_default="False")
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys
    id_department = Column(Integer, ForeignKey("refer.department.id"), nullable=False)
    id_schedule = Column(Integer, ForeignKey("refer.schedule.id"), nullable=False)
    # relations
    department = relationship("Department", back_populates="roles")
    schedule = relationship("Schedule", back_populates="roles")
    user_roles = relationship("User_Role", back_populates="role", cascade="all, delete-orphan")

    # dict class
    def to_dict(self):
        return {"id": self.id, "name": self.name, "type": self.type, "create_date": self.create_date,
                "update_date": self.update_date, "status": self.status,
                "log_date": self.log_date.isoformat() if self.log_date else None}


class User_Role(BASE):
    __tablename__ = "user_role"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, Identity(start=500, increment=1, cycle=False), primary_key=True)
    status = Column(Boolean, nullable=False, server_default="False")
    log_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    # foreign keys
    id_user = Column(Integer, ForeignKey("auth.user.id"), nullable=False)
    id_rol = Column(Integer, ForeignKey("refer.role.id"), nullable=False)
    # relations
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")

    # dict class
    def to_dict(self):
        return {"id": self.id, "status": self.status, "log_date": self.log_date.isoformat() if self.log_date else None}
