-- public.alertas_florestas definition

-- Drop table

-- DROP TABLE public.alertas_florestas;

CREATE TABLE public.alertas_florestas (
	id bigserial NOT NULL,
	geom geometry(POINT, 4326) NULL,
	datahora varchar(80) NULL,
	satelite varchar(80) NULL,
	pais varchar(80) NULL,
	estado varchar(80) NULL,
	municipio varchar(80) NULL,
	bioma varchar(50) NULL,
	diasemchuv int4 NULL,
	precipitac numeric(20,8) NULL,
	riscofogo numeric(20,8) NULL,
	latitude numeric(20,8) NULL,
	longitude numeric(20,8) NULL,
	frp numeric(20,8) NULL,
	cnfp_id int4 NULL,
	objectid int8 NULL,
	nome varchar(200) NULL,
	orgao varchar(100) NULL,
	classe varchar(30) NULL,
	estagio varchar(30) NULL,
	governo varchar(20) NULL,
	codigo varchar(30) NULL,
	ano int8 NULL,
	uf varchar(4) NULL,
	protecao varchar(30) NULL,
	tipo varchar(40) NULL,
	comunitari varchar(6) NULL,
	atolegal varchar(100) NULL,
	anocriacao int8 NULL,
	categoria varchar(40) NULL,
	observacao varchar(200) NULL,
	sobreposic varchar(3) NULL,
	area_ha int8 NULL,
	CONSTRAINT alertas_florestas_pkey PRIMARY KEY (id)
);
CREATE INDEX alertas_florestas_geom_id ON public.alertas_florestas USING gist (geom);


-- public.auth_group definition

-- Drop table

-- DROP TABLE public.auth_group;

CREATE TABLE public.auth_group (
	id serial NOT NULL,
	"name" varchar(150) NOT NULL,
	CONSTRAINT auth_group_name_key UNIQUE (name),
	CONSTRAINT auth_group_pkey PRIMARY KEY (id)
);
CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


-- public.auth_user definition

-- Drop table

-- DROP TABLE public.auth_user;

CREATE TABLE public.auth_user (
	id serial NOT NULL,
	"password" varchar(128) NOT NULL,
	last_login timestamptz NULL,
	is_superuser bool NOT NULL,
	username varchar(150) NOT NULL,
	first_name varchar(150) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff bool NOT NULL,
	is_active bool NOT NULL,
	date_joined timestamptz NOT NULL,
	CONSTRAINT auth_user_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_username_key UNIQUE (username)
);
CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


-- public.cnfp definition

-- Drop table

-- DROP TABLE public.cnfp;

CREATE TABLE public.cnfp (
	id bigserial NOT NULL,
	geom geometry(MULTIPOLYGON, 4326) NULL,
	objectid int8 NULL,
	nome varchar(200) NULL,
	orgao varchar(100) NULL,
	classe varchar(30) NULL,
	estagio varchar(30) NULL,
	governo varchar(20) NULL,
	codigo varchar(30) NULL,
	ano int8 NULL,
	uf varchar(4) NULL,
	protecao varchar(30) NULL,
	tipo varchar(40) NULL,
	comunitari varchar(6) NULL,
	atolegal varchar(100) NULL,
	anocriacao int8 NULL,
	categoria varchar(40) NULL,
	observacao varchar(200) NULL,
	sobreposic varchar(3) NULL,
	bioma varchar(50) NULL,
	shape_leng float8 NULL,
	shape_area float8 NULL,
	area_ha int8 NULL,
	layer varchar(100) NULL,
	CONSTRAINT cnfp_pkey PRIMARY KEY (id)
);
CREATE INDEX cnfp_geom_id ON public.cnfp USING gist (geom);


-- public.django_content_type definition

-- Drop table

-- DROP TABLE public.django_content_type;

CREATE TABLE public.django_content_type (
	id serial NOT NULL,
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model),
	CONSTRAINT django_content_type_pkey PRIMARY KEY (id)
);


-- public.django_migrations definition

-- Drop table

-- DROP TABLE public.django_migrations;

CREATE TABLE public.django_migrations (
	id bigserial NOT NULL,
	app varchar(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	applied timestamptz NOT NULL,
	CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);


-- public.django_session definition

-- Drop table

-- DROP TABLE public.django_session;

CREATE TABLE public.django_session (
	session_key varchar(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamptz NOT NULL,
	CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


-- public.email_mp definition

-- Drop table

-- DROP TABLE public.email_mp;

CREATE TABLE public.email_mp (
	id bigserial NOT NULL,
	uf varchar(200) NULL,
	email varchar(254) NOT NULL,
	CONSTRAINT email_mp_pkey PRIMARY KEY (id)
);


-- public.focos_incendio_inpe definition

-- Drop table

-- DROP TABLE public.focos_incendio_inpe;

CREATE TABLE public.focos_incendio_inpe (
	id bigserial NOT NULL,
	geom geometry(POINT, 4326) NULL,
	datahora varchar(80) NULL,
	satelite varchar(80) NULL,
	pais varchar(80) NULL,
	estado varchar(80) NULL,
	municipio varchar(80) NULL,
	bioma varchar(80) NULL,
	diasemchuv int4 NULL,
	precipitac numeric(20,8) NULL,
	riscofogo numeric(20,8) NULL,
	latitude numeric(20,8) NULL,
	longitude numeric(20,8) NULL,
	frp numeric(20,8) NULL,
	cnfp_id int4 NULL,
	CONSTRAINT focos_incendio_inpe_pkey PRIMARY KEY (id)
);
CREATE INDEX focos_incendio_inpe_geom_id ON public.focos_incendio_inpe USING gist (geom);


-- public.spatial_ref_sys definition

-- Drop table

-- DROP TABLE public.spatial_ref_sys;

CREATE TABLE public.spatial_ref_sys (
	srid int4 NOT NULL,
	auth_name varchar(256) NULL,
	auth_srid int4 NULL,
	srtext varchar(2048) NULL,
	proj4text varchar(2048) NULL,
	CONSTRAINT spatial_ref_sys_pkey PRIMARY KEY (srid),
	CONSTRAINT spatial_ref_sys_srid_check CHECK (((srid > 0) AND (srid <= 998999)))
);


-- public.tipo_penal definition

-- Drop table

-- DROP TABLE public.tipo_penal;

CREATE TABLE public.tipo_penal (
	id bigserial NOT NULL,
	tipo_penal varchar(50) NOT NULL,
	lei varchar(50) NOT NULL,
	descricao text NOT NULL,
	CONSTRAINT tipo_penal_pkey PRIMARY KEY (id)
);


-- public.auth_permission definition

-- Drop table

-- DROP TABLE public.auth_permission;

CREATE TABLE public.auth_permission (
	id serial NOT NULL,
	"name" varchar(255) NOT NULL,
	content_type_id int4 NOT NULL,
	codename varchar(100) NOT NULL,
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
	CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
	CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


-- public.auth_user_groups definition

-- Drop table

-- DROP TABLE public.auth_user_groups;

CREATE TABLE public.auth_user_groups (
	id bigserial NOT NULL,
	user_id int4 NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id),
	CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


-- public.auth_user_user_permissions definition

-- Drop table

-- DROP TABLE public.auth_user_user_permissions;

CREATE TABLE public.auth_user_user_permissions (
	id bigserial NOT NULL,
	user_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
	CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


-- public.django_admin_log definition

-- Drop table

-- DROP TABLE public.django_admin_log;

CREATE TABLE public.django_admin_log (
	id serial NOT NULL,
	action_time timestamptz NOT NULL,
	object_id text NULL,
	object_repr varchar(200) NOT NULL,
	action_flag int2 NOT NULL,
	change_message text NOT NULL,
	content_type_id int4 NULL,
	user_id int4 NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0)),
	CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
	CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


-- public.noticia_crime definition

-- Drop table

-- DROP TABLE public.noticia_crime;

CREATE TABLE public.noticia_crime (
	id bigserial NOT NULL,
	user_email varchar(254) NOT NULL,
	url_doc varchar(256) NOT NULL,
	data_documento timestamptz NOT NULL,
	documento text NOT NULL,
	alerta_florestal_id int8 NOT NULL,
	email_mp_id int8 NOT NULL,
	tipo_penal_id int8 NOT NULL,
	CONSTRAINT noticia_crime_pkey PRIMARY KEY (id),
	CONSTRAINT noticia_crime_alerta_florestal_id_e8b72b85_fk_alertas_f FOREIGN KEY (alerta_florestal_id) REFERENCES public.alertas_florestas(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT noticia_crime_email_mp_id_aa4d0acc_fk_email_mp_id FOREIGN KEY (email_mp_id) REFERENCES public.email_mp(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT noticia_crime_tipo_penal_id_7441fc46_fk_tipo_penal_id FOREIGN KEY (tipo_penal_id) REFERENCES public.tipo_penal(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX noticia_crime_alerta_florestal_id_e8b72b85 ON public.noticia_crime USING btree (alerta_florestal_id);
CREATE INDEX noticia_crime_email_mp_id_aa4d0acc ON public.noticia_crime USING btree (email_mp_id);
CREATE INDEX noticia_crime_tipo_penal_id_7441fc46 ON public.noticia_crime USING btree (tipo_penal_id);


-- public.auth_group_permissions definition

-- Drop table

-- DROP TABLE public.auth_group_permissions;

CREATE TABLE public.auth_group_permissions (
	id bigserial NOT NULL,
	group_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
	CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);