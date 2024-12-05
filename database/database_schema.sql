--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: members; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.members (
    member_id character(9) NOT NULL,
    name character varying(25) NOT NULL,
    street_address character varying(25) NOT NULL,
    city character varying(14) NOT NULL,
    state character(2) NOT NULL,
    zip_code character(5) NOT NULL,
    status character varying(10) DEFAULT 'active'::character varying,
    CONSTRAINT members_status_check CHECK (((status)::text = ANY ((ARRAY['active'::character varying, 'suspended'::character varying])::text[])))
);


ALTER TABLE public.members OWNER TO postgres;

--
-- Name: providers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.providers (
    provider_id character(9) NOT NULL,
    name character varying(25) NOT NULL,
    street_address character varying(25) NOT NULL,
    city character varying(14) NOT NULL,
    state character(2) NOT NULL,
    zip_code character(5) NOT NULL
);


ALTER TABLE public.providers OWNER TO postgres;

--
-- Name: service_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_records (
    record_id integer NOT NULL,
    current_date_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    service_date date NOT NULL,
    provider_id character(9),
    member_id character(9),
    service_code character(6),
    comments character varying(100),
    CONSTRAINT valid_service_date CHECK ((service_date <= CURRENT_DATE))
);


ALTER TABLE public.service_records OWNER TO postgres;


--
-- Name: service_records_record_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_records_record_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.service_records_record_id_seq OWNER TO postgres;

--
-- Name: service_records_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_records_record_id_seq OWNED BY public.service_records.record_id;


--
-- Name: service_records record_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_records ALTER COLUMN record_id SET DEFAULT nextval('public.service_records_record_id_seq'::regclass);
--
-- Name: services; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.services (
    service_code character(6) NOT NULL,
    service_name character varying(20) NOT NULL,
    fee numeric(6,2),
    CONSTRAINT services_fee_check CHECK ((fee <= 999.99))
);


ALTER TABLE public.services OWNER TO postgres;

--
-- Name: weekly_provider_reports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weekly_provider_reports (
    report_id serial PRIMARY KEY,  -- Automatically generates a unique report ID
    provider_id character(9) NOT NULL,  -- Foreign key to providers table
    week_end_date date NOT NULL,  -- The week end date for the report
    total_consultations integer CHECK (total_consultations <= 999),  -- Total consultations (3 digits)
    total_fees numeric(8,2) CHECK (total_fees <= 99999.99),  -- Total fees (up to $99,999.99)
    CONSTRAINT weekly_provider_reports_provider_id_fkey FOREIGN KEY (provider_id)
        REFERENCES public.providers(provider_id) ON DELETE CASCADE  -- Foreign key referencing providers table
);


ALTER TABLE public.weekly_provider_reports OWNER TO postgres;


--
-- Name: weekly_provider_reports_report_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.weekly_provider_reports_report_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.weekly_provider_reports_report_id_seq OWNER TO postgres;

--
-- Name: weekly_provider_reports_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.weekly_provider_reports_report_id_seq OWNED BY public.weekly_provider_reports.report_id;


--
-- Name: service_records record_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weekly_provider_reports ALTER COLUMN report_id SET DEFAULT nextval('public.weekly_provider_reports_report_id_seq'::regclass);

--
-- Name: eft_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eft_records (
    transaction_id serial PRIMARY KEY,  -- Automatically generates a unique transaction ID
    provider_id character(9) NOT NULL,  -- Foreign key to providers table
    amount numeric(10,2) NOT NULL CHECK (amount <= 999999.99),  -- Amount (up to $999,999.99)
    transfer_date date NOT NULL,  -- The date of the transfer
    CONSTRAINT eft_records_provider_id_fkey FOREIGN KEY (provider_id)
        REFERENCES public.providers(provider_id) ON DELETE CASCADE  -- Foreign key referencing providers table
);

ALTER TABLE public.eft_records OWNER TO postgres;

--- create sequence ---
CREATE SEQUENCE public.eft_records_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.eft_records_transaction_id_seq OWNER TO postgres;

--
-- Name: weekly_provider_reports_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eft_records_transaction_id_seq OWNED BY public.eft_records.transaction_id;


--
-- Name: service_records record_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eft_records ALTER COLUMN transaction_id SET DEFAULT nextval('public.eft_records_transaction_id_seq'::regclass);


--
-- Name: members members_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (member_id);


--
-- Name: providers providers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.providers
    ADD CONSTRAINT providers_pkey PRIMARY KEY (provider_id);


--
-- Name: service_records service_records_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_records
    ADD CONSTRAINT service_records_pkey PRIMARY KEY (record_id);


--
-- Name: services services_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (service_code);


--
-- Name: service_records service_records_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_records
    ADD CONSTRAINT service_records_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.members(member_id);


--
-- Name: service_records service_records_provider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_records
    ADD CONSTRAINT service_records_provider_id_fkey FOREIGN KEY (provider_id) REFERENCES public.providers(provider_id);


--
-- Name: service_records service_records_service_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_records
    ADD CONSTRAINT service_records_service_code_fkey FOREIGN KEY (service_code) REFERENCES public.services(service_code);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO dev;


--
-- Name: TABLE members; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.members TO dev;


--
-- Name: TABLE providers; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.providers TO dev;

--
-- Name: TABLE eft_records; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.weekly_provider_reports TO dev;
--
-- Name: SEQUENCE service_records_record_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.service_records_record_id_seq TO dev;


--
-- Name: TABLE services; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.services TO dev;


--
-- Name: TABLE service_records; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.service_records TO dev;

--
-- Name: TABLE weekly_provider_reports; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.eft_records TO dev;

--
-- PostgreSQL database dump complete
--

