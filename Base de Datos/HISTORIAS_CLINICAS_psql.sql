/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     13/05/2016 23:43:57                          */
/*==============================================================*/


drop index PROVINCIA_CANTON_FK;

drop index CANTON_PK;

drop table CANTON;

drop index CONTACTO_PARROQUIA_FK;

drop index CONTACTO_PK;

drop table CONTACTO;

drop index HISTORIA_CONTACTO_FK;

drop index HISTORIA_PACIENTE_FK;

drop index HISTORIA_CLINICA_PK;

drop table HISTORIA_CLINICA;

drop index PACIENTE_PARROQUIA_ACTUAL_FK;

drop index PACIENTE_CANTON_NACIMIENTO_FK;

drop index PACIENTE_TIPO_BENEFICIARIO_FK;

drop index PACIENTE_PK;

drop table PACIENTE;

drop index PAIS_PK;

drop table PAIS;

drop index CANTON_PARROQUIA_FK;

drop index PARROQUIA_PK;

drop table PARROQUIA;

drop index PAIS_PROVINCIA_FK;

drop index PROVINCIA_PK;

drop table PROVINCIA;

drop index TIPO_BENEFICIARIO_PK;

drop table TIPO_BENEFICIARIO;

/*==============================================================*/
/* Table: CANTON                                                */
/*==============================================================*/
create table CANTON (
   CAN_CODIGO           VARCHAR(10)          not null,
   PRO_CODIGO           VARCHAR(10)          null,
   CAN_NOMBRE           VARCHAR(60)          null,
   constraint PK_CANTON primary key (CAN_CODIGO)
);

/*==============================================================*/
/* Index: CANTON_PK                                             */
/*==============================================================*/
create unique index CANTON_PK on CANTON (
CAN_CODIGO
);

/*==============================================================*/
/* Index: PROVINCIA_CANTON_FK                                   */
/*==============================================================*/
create  index PROVINCIA_CANTON_FK on CANTON (
PRO_CODIGO
);

/*==============================================================*/
/* Table: CONTACTO                                              */
/*==============================================================*/
create table CONTACTO (
   CON_CODIGO           INT4                 not null,
   PAR_CODIGO           VARCHAR(10)          null,
   CON_NOMBRE           VARCHAR(60)          null,
   CON_TELEFONO         VARCHAR(12)          null,
   CON_TRABAJO          VARCHAR(60)          null,
   constraint PK_CONTACTO primary key (CON_CODIGO)
);

/*==============================================================*/
/* Index: CONTACTO_PK                                           */
/*==============================================================*/
create unique index CONTACTO_PK on CONTACTO (
CON_CODIGO
);

/*==============================================================*/
/* Index: CONTACTO_PARROQUIA_FK                                 */
/*==============================================================*/
create  index CONTACTO_PARROQUIA_FK on CONTACTO (
PAR_CODIGO
);

/*==============================================================*/
/* Table: HISTORIA_CLINICA                                      */
/*==============================================================*/
create table HISTORIA_CLINICA (
   HIS_CODIGO           VARCHAR(12)          not null,
   PAC_CEDULA           VARCHAR(10)          null,
   CON_CODIGO           INT4                 null,
   HIS_FECHA_CREACION   DATE                 null,
   HIS_HORA_CREACION    TIME                 null,
   constraint PK_HISTORIA_CLINICA primary key (HIS_CODIGO)
);

/*==============================================================*/
/* Index: HISTORIA_CLINICA_PK                                   */
/*==============================================================*/
create unique index HISTORIA_CLINICA_PK on HISTORIA_CLINICA (
HIS_CODIGO
);

/*==============================================================*/
/* Index: HISTORIA_PACIENTE_FK                                  */
/*==============================================================*/
create  index HISTORIA_PACIENTE_FK on HISTORIA_CLINICA (
PAC_CEDULA
);

/*==============================================================*/
/* Index: HISTORIA_CONTACTO_FK                                  */
/*==============================================================*/
create  index HISTORIA_CONTACTO_FK on HISTORIA_CLINICA (
CON_CODIGO
);

/*==============================================================*/
/* Table: PACIENTE                                              */
/*==============================================================*/
create table PACIENTE (
   PAC_CEDULA           VARCHAR(10)          not null,
   TIP_CODIGO           VARCHAR(4)           null,
   CAN_CODIGO           VARCHAR(10)          null,
   PAR_CODIGO           VARCHAR(10)          null,
   PAC_CODIGO           VARCHAR(15)          null,
   PAC_NOMBRE           VARCHAR(60)          null,
   PAC_FECHA_NAC        DATE                 null,
   SEXO                 VARCHAR(1)           null,
   PAC_DIRECCION        TEXT                 null,
   PAC_TELEFONO         VARCHAR(12)          null,
   constraint PK_PACIENTE primary key (PAC_CEDULA)
);

/*==============================================================*/
/* Index: PACIENTE_PK                                           */
/*==============================================================*/
create unique index PACIENTE_PK on PACIENTE (
PAC_CEDULA
);

/*==============================================================*/
/* Index: PACIENTE_TIPO_BENEFICIARIO_FK                         */
/*==============================================================*/
create  index PACIENTE_TIPO_BENEFICIARIO_FK on PACIENTE (
TIP_CODIGO
);

/*==============================================================*/
/* Index: PACIENTE_CANTON_NACIMIENTO_FK                         */
/*==============================================================*/
create  index PACIENTE_CANTON_NACIMIENTO_FK on PACIENTE (
CAN_CODIGO
);

/*==============================================================*/
/* Index: PACIENTE_PARROQUIA_ACTUAL_FK                          */
/*==============================================================*/
create  index PACIENTE_PARROQUIA_ACTUAL_FK on PACIENTE (
PAR_CODIGO
);

/*==============================================================*/
/* Table: PAIS                                                  */
/*==============================================================*/
create table PAIS (
   PAI_CODIGO           VARCHAR(5)           not null,
   PAI_NOMBRE           VARCHAR(60)          null,
   constraint PK_PAIS primary key (PAI_CODIGO)
);

/*==============================================================*/
/* Index: PAIS_PK                                               */
/*==============================================================*/
create unique index PAIS_PK on PAIS (
PAI_CODIGO
);

/*==============================================================*/
/* Table: PARROQUIA                                             */
/*==============================================================*/
create table PARROQUIA (
   PAR_CODIGO           VARCHAR(10)          not null,
   CAN_CODIGO           VARCHAR(10)          null,
   PAR_NOMBRE           VARCHAR(60)          null,
   constraint PK_PARROQUIA primary key (PAR_CODIGO)
);

/*==============================================================*/
/* Index: PARROQUIA_PK                                          */
/*==============================================================*/
create unique index PARROQUIA_PK on PARROQUIA (
PAR_CODIGO
);

/*==============================================================*/
/* Index: CANTON_PARROQUIA_FK                                   */
/*==============================================================*/
create  index CANTON_PARROQUIA_FK on PARROQUIA (
CAN_CODIGO
);

/*==============================================================*/
/* Table: PROVINCIA                                             */
/*==============================================================*/
create table PROVINCIA (
   PRO_CODIGO           VARCHAR(10)          not null,
   PAI_CODIGO           VARCHAR(5)           null,
   PRO_NOMBRE           VARCHAR(60)          null,
   constraint PK_PROVINCIA primary key (PRO_CODIGO)
);

/*==============================================================*/
/* Index: PROVINCIA_PK                                          */
/*==============================================================*/
create unique index PROVINCIA_PK on PROVINCIA (
PRO_CODIGO
);

/*==============================================================*/
/* Index: PAIS_PROVINCIA_FK                                     */
/*==============================================================*/
create  index PAIS_PROVINCIA_FK on PROVINCIA (
PAI_CODIGO
);

/*==============================================================*/
/* Table: TIPO_BENEFICIARIO                                     */
/*==============================================================*/
create table TIPO_BENEFICIARIO (
   TIP_CODIGO           VARCHAR(4)           not null,
   TIP_NOMBRE           VARCHAR(60)          null,
   constraint PK_TIPO_BENEFICIARIO primary key (TIP_CODIGO)
);

/*==============================================================*/
/* Index: TIPO_BENEFICIARIO_PK                                  */
/*==============================================================*/
create unique index TIPO_BENEFICIARIO_PK on TIPO_BENEFICIARIO (
TIP_CODIGO
);

alter table CANTON
   add constraint FK_CANTON_PROVINCIA_PROVINCI foreign key (PRO_CODIGO)
      references PROVINCIA (PRO_CODIGO)
      on delete restrict on update restrict;

alter table CONTACTO
   add constraint FK_CONTACTO_CONTACTO__PARROQUI foreign key (PAR_CODIGO)
      references PARROQUIA (PAR_CODIGO)
      on delete restrict on update restrict;

alter table HISTORIA_CLINICA
   add constraint FK_HISTORIA_HISTORIA__CONTACTO foreign key (CON_CODIGO)
      references CONTACTO (CON_CODIGO)
      on delete restrict on update restrict;

alter table HISTORIA_CLINICA
   add constraint FK_HISTORIA_HISTORIA__PACIENTE foreign key (PAC_CEDULA)
      references PACIENTE (PAC_CEDULA)
      on delete restrict on update restrict;

alter table PACIENTE
   add constraint FK_PACIENTE_PACIENTE__CANTON foreign key (CAN_CODIGO)
      references CANTON (CAN_CODIGO)
      on delete restrict on update restrict;

alter table PACIENTE
   add constraint FK_PACIENTE_PACIENTE__PARROQUI foreign key (PAR_CODIGO)
      references PARROQUIA (PAR_CODIGO)
      on delete restrict on update restrict;

alter table PACIENTE
   add constraint FK_PACIENTE_PACIENTE__TIPO_BEN foreign key (TIP_CODIGO)
      references TIPO_BENEFICIARIO (TIP_CODIGO)
      on delete restrict on update restrict;

alter table PARROQUIA
   add constraint FK_PARROQUI_CANTON_PA_CANTON foreign key (CAN_CODIGO)
      references CANTON (CAN_CODIGO)
      on delete restrict on update restrict;

alter table PROVINCIA
   add constraint FK_PROVINCI_PAIS_PROV_PAIS foreign key (PAI_CODIGO)
      references PAIS (PAI_CODIGO)
      on delete restrict on update restrict;

