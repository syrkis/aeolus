-- Save the results into a .sql file
-- Filename: extract_data.sql

copy (
    SELECT 
        (tags -> 'voltage') AS voltage,
        (tags -> 'cables') AS cables,
        ST_AsText(way) AS location
    FROM 
        planet_osm_line 
    WHERE 
        power = 'line' 
        AND (tags ? 'voltage') 
        AND (string_to_array(tags -> 'voltage', ';'))::int[] @> ARRAY[400000]
) 
TO '/Users/syrkis/data/aeolus/infrastructure/power_lines.csv' WITH CSV HEADER;

copy (
    SELECT 
        name,
        highway,
        ST_AsText(way) AS location
    FROM planet_osm_line
    WHERE highway IS NOT NULL
)
TO '/Users/syrkis/data/aeolus/infrastructure/highways.csv' WITH CSV HEADER;

copy (
    SELECT 
        power, 
        (tags -> 'name') AS name, 
        (tags -> 'operator') AS operator, 
        ST_AsText(way) AS location 
    FROM 
        planet_osm_point 
    WHERE 
        power IS NOT NULL
)
TO '/Users/syrkis/data/aeolus/infrastructure/power_infrastructure.csv' WITH CSV HEADER;

copy (
    SELECT 
        (tags -> 'name') AS name,
        (tags -> 'plant:source') AS source,
        (tags -> 'plant:output:electricity') AS output,
        ST_AsText(way) AS location
    FROM 
        planet_osm_point 
    WHERE 
        power='plant'
)
TO '/Users/syrkis/data/aeolus/infrastructure/power_plants.csv' WITH CSV HEADER;

copy (
    SELECT 
        name, 
        boundary,
        landuse,
        leisure,
        ST_AsText(way) AS location
    FROM 
        planet_osm_polygon 
    WHERE 
        leisure='park' OR boundary='protected_area' OR landuse='conservation'
) 
TO '/Users/syrkis/data/aeolus/infrastructure/protected_areas.csv' WITH CSV HEADER;

copy (
    SELECT 
        name, 
        aeroway,
        ST_AsText(way) AS location
    FROM 
        planet_osm_polygon 
    WHERE 
        aeroway='aerodrome'
) 
TO '/Users/syrkis/data/aeolus/infrastructure/airports.csv' WITH CSV HEADER;
