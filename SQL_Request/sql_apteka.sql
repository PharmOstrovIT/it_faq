CREATE TABLE IF NOT EXISTS public.main_apteka
(
    id integer NOT NULL DEFAULT nextval('apteka_id_seq'::regclass),
    name character varying(12) COLLATE pg_catalog."default" NOT NULL,
    region character varying(200) COLLATE pg_catalog."default" NOT NULL,
    city_name character varying(200) COLLATE pg_catalog."default" NOT NULL,
    address character varying(200) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(200) COLLATE pg_catalog."default" NOT NULL,
    mobile_phone character varying(200) COLLATE pg_catalog."default" NOT NULL,
    organization character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT apteka_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_apteka
    OWNER to postgres;
    
    
CREATE TABLE IF NOT EXISTS public.main_cartridge
(
    id integer NOT NULL DEFAULT nextval('main_cartridge_id_seq'::regclass),
    apteka_id integer,
    printer character varying(200) COLLATE pg_catalog."default",
    cartridge character varying(200) COLLATE pg_catalog."default",
    cartridge_num character varying(200) COLLATE pg_catalog."default",
    service_date character varying(200) COLLATE pg_catalog."default",
    writeoff_date character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT main_cartridge_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_cartridge
    OWNER to postgres;
    
    
CREATE TABLE IF NOT EXISTS public.main_equipment
(
    id integer NOT NULL DEFAULT nextval('main_equipment_id_seq'::regclass),
    apteka_id integer NOT NULL,
    equipment_type character varying(200) COLLATE pg_catalog."default" NOT NULL,
    equipment_model character varying(200) COLLATE pg_catalog."default" NOT NULL,
    serial_number character varying(200) COLLATE pg_catalog."default",
    invoice_number character varying(200) COLLATE pg_catalog."default",
    invoice_date date,
    purchase_org character varying(200) COLLATE pg_catalog."default",
    comments character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT main_equipment_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_equipment
    OWNER to postgres;
    
    
CREATE TABLE IF NOT EXISTS public.main_security
(
    id integer NOT NULL DEFAULT nextval('main_security_id_seq'::regclass),
    apteka_id integer,
    service_name character varying(200) COLLATE pg_catalog."default",
    service_ip character varying(200) COLLATE pg_catalog."default",
    service_login character varying(200) COLLATE pg_catalog."default",
    service_pass character varying(200) COLLATE pg_catalog."default",
    service_info character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT main_security_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main_security
    OWNER to postgres;