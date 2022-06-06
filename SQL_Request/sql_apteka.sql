CREATE TABLE public.main_apteka
(
    id serial NOT NULL,
    name varchar(12) NOT NULL,
    region varchar(200) NOT NULL,
    city_name varchar(200) NOT NULL,
    address varchar(200) NOT NULL,
    phone varchar(200) NOT NULL,
    mobile_phone varchar(200) NOT NULL,
    organization varchar(200) NOT NULL,
    PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_apteka
    OWNER to postgres;
    
    
CREATE TABLE public.main_equipment
(
    id serial NOT NULL,
    apteka_id int NOT NULL,
    equipment_type varchar(200) NOT NULL,
    equipment_model varchar(200) NOT NULL,
    serial_number varchar(200),
    purchase_date date NOT NULL,
    invoice_number varchar(200) NOT NULL,
    invoice_date date NOT NULL,
    purchase_org varchar(200) NOT NULL,
    comments varchar(200) NOT NULL,
    PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_equipment
    OWNER to postgres;