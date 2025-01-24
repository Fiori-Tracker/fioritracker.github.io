---
title: Full installation order
description: 'Install the components in the described order by following linked component-specific guides.'
---
# Full installation order

{#- Define modules, their order and containers for types of values -#}
{%- set module_names = ['core', 'asisCen', 'ro', 'tu', 'fa', 'fr', 'ai'] -%}
{%- set storage = { 'fnode': [], 'odata': [], 'ro': [] } -%}

{%- for module_name in module_names -%}
  {%- set module = prod[module_name] -%}
  {%- for key, value in module.items() -%}
    {%- set value_ns = namespace(array=[]) -%}
    {%- if key in storage and value -%}
      {#- The values are strings with comma separated lists -#}
      {%- for part in value.split(",") -%}
        {#- Add the 'code' ticks to the string entries -#}
        {%- set _ = value_ns.array.append('`' ~ part.strip() ~ '`') -%}
      {%- endfor -%}
      {%- set _ = storage[key].extend(value_ns.array) -%}
    {%- endif -%}
  {%- endfor -%}
{%- endfor %}

1. [Obtain the and import](inst/step-1.md) transports files

2. [Activate Frontend ICF nodes](inst/step-2.md): {{ ", ".join(storage['fnode']) }}

3. [Enable backend oData services](inst/step-3.md): {{ ", ".join(storage['odata']) }}

4. [Assign pfcg roles](inst/step-4.md): {{ ", ".join(storage['ro']) }}

5. [Set the parameters for activation key and log mode](inst/step-5.md)



