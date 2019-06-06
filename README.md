TU Libraries Ansible Role for Networking
=========

This is a role to overlay application- or subsystem-specific networking rules.

It is applied to specific infrastructure via Playbook's use of hosts with the role's invocation.

Requirements
------------

Use `Pipenv` and `.python-version` files to know the required libraries to run this role.

Role Variables
--------------

### Internal Zone
- `internal_services`: list of defined services you want to enable for the internal firewalld zone. Defaults to `[]`
- `internal_sources`: list of IPs that you want to enable access over the internal firewalld zone. Defaults to `[]`
- `internal_ports`: list of ports that you want to enable access to over the internal firewalld zone. Defaults to `[]`
- `internal_rich_rules`: list of rich rules you want to enable for the internal firewalld zone. Defaults to `[]`

### Trusted Zone
- `trusted_services`: list of defined services you want to enable for the trusted firewalld zone. Defaults to `[]`
- `trusted_sources`: list of IPs that you want to enable access over the trusted firewalld zone. Defaults to `[]`
- `trusted_ports`: list of ports that you want to enable access to over the trusted firewalld zone. Defaults to `[]`
- `trusted_rich_rules`: list of rich rules you want to enable for the trusted firewalld zone. Defaults to `[]`


### Public Zone
- `public_services`: list of defined services you want to enable for the public firewalld zone. Defaults to `[]`
- `public_ports`: list of ports that you want to enable access to over the public firewalld zone. Defaults to `[]`
- `public_rich_rules`: list of rich rules you want to enable for the public firewalld zone. Defaults to `[]`
- `public_sources`: list of IPs that you want to enable access over the public firewalld zone. Defaults to `[]`

[Docs on firewalld zones](https://firewalld.org/documentation/man-pages/firewalld.zones.html)

Dependencies
------------

This role requires no other roles or libraries. It works through the `firewalld` ansible module.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: networking
           public_services: https


License
-------

BSD
