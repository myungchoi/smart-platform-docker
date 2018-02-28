psql -U postgres -d postgres -a -f /opt/data/create_user.sql
psql -U postgres postgres < /opt/data/omop_v5_dump.tgz
psql -U postgres -d postgres -a -f /opt/data/update_seqs.sql
rm -rf /opt/data/*
