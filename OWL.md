# OWL


# State
State is a object that is used to contain data or information about the component.



# Component Properties

There are several component properties are avialble

1. **template**: Name of the template which design in `XML`
2. **props**: Properties of the components, props will be object which will contain `type` and `optional` for additional information.
3. **defaultProps**: Default value for a props  
4. **displayType**: This information is additional
5. **supportedTypes**: Additional information
6. **isEmpty**: Additional information
7. **extractProps**: Additional information about props
8. **components**: Component which will be used for display.


## Standard Props
There are several standard props available in OWL 

```bash 
const standardFieldProps = {
    id: { type: String, optional: true },
    name: { type: String, optional: true },
    readonly: { type: Boolean, optional: true },
    record: { type: Object, optional: true },
    type: { type: String, optional: true },
    update: { type: Function, optional: true },
    value: true,
    decorations: { type: Object, optional: true },
    setDirty: { type: Function, optional: true },
};
```

- id
- name 
- readonly
- record
- type
- update
- value
- decorations
- setDirty

Along with these standard props field can use additional props to meet specific requirements.



# Fields 





# ODOO View Design Common Format

```xml

  <div class="o_action_manager">
    <div class="o_action o_view_controller o_list_view">
 <!-- Header Section -->
      <div class="o_control_panel">
        <div class="o_cp_top">
          <div class="o_cp_top_left">Left Header Top</div>
          <div class="o_cp_top_right">Right Header Top</div>
        </div>
        <div class="o_cp_bottom">
          <div class="o_cp_bottom_left">Left Header Bottom</div>
          <div class="o_cp_bottom_right">Right Header Bottom</div>
        </div>
      </div>
 <!-- Main Section -->
      <div class="o_content">
        <div class="o_list_renderer o_renderer table-responsive">
          Main  Content
        </div>
      </div>
    </div>
  </div>


```




# ODOO Model

Odoo uses an Abstract Class to implement its class architecture. Defination of odoo model available in `odoo/odoo/models.py`. 

```xml

BaseModel --> AbstractModel --> Model

```

All the function defination of odoo function or method are available in `BaseModel`. Some of them are important in daily life uses

## Methods
- mapped `records.mapped(lambda r: r.field1 + r.field2)`
- sorted `records.sorted(key=lambda r: r.name)`
- filtered `records.filtered(lambda r: r.company_id == user.company_id)`
- filtered_domain 
- with_context 
- with_company
- with_user
- sudo
- with_env
- ensure_one
- browse
- toggle_active
- action_archive
- action_unarchive
- search_read
- exists
- copy
- create
- write
- unlink
- get_base_url
- get_metadata
- get_field_translations
- update_field_translations
- read
- check_field_access_rights
- fields_get
- init
- read_group
- clear_caches
- name_search
- name_create
- name_get
- search
- search_count
- user_has_groups
- fields_get_keys
- default_get
- load
- export_data
- 

## Attributes

    _name = None                #: the model name (in dot-notation, module namespace)
    _description = None         #: the model's informal name
    _module = None              #: the model's module (in the Odoo sense)
    _custom = False             #: should be True for custom models only

    _inherit = ()
    """Python-inherited models:

    :type: str or list(str)

    .. note::

        * If :attr:`._name` is set, name(s) of parent models to inherit from
        * If :attr:`._name` is unset, name of a single model to extend in-place
    """
    _inherits = frozendict()
    """dictionary {'parent_model': 'm2o_field'} mapping the _name of the parent business
    objects to the names of the corresponding foreign key fields to use::

      _inherits = {
          'a.model': 'a_field_id',
          'b.model': 'b_field_id'
      }

    implements composition-based inheritance: the new model exposes all
    the fields of the inherited models but stores none of them:
    the values themselves remain stored on the linked record.

    .. warning::

      if multiple fields with the same name are defined in the
      :attr:`~odoo.models.Model._inherits`-ed models, the inherited field will
      correspond to the last one (in the inherits list order).
    """
    _table = None               #: SQL table name used by model if :attr:`_auto`
    _table_query = None         #: SQL expression of the table's content (optional)
    _sql_constraints = []       #: SQL constraints [(name, sql_def, message)]

    _rec_name = None            #: field to use for labeling records, default: ``name``
    _rec_names_search = None    #: fields to consider in ``name_search``
    _order = 'id'               #: default order field for searching results
    _parent_name = 'parent_id'  #: the many2one field used as parent field
    _parent_store = False
    """set to True to compute parent_path field.

    Alongside a :attr:`~.parent_path` field, sets up an indexed storage
    of the tree structure of records, to enable faster hierarchical queries
    on the records of the current model using the ``child_of`` and
    ``parent_of`` domain operators.
    """
    _active_name = None
    """field to use for active records, automatically set to either ``"active"``
    or ``"x_active"``.
    """




# Database Field Type

Fields used with odoo model and it creates database field in database. There are several fields avilable in odoo.

In Odoo Field architecure, an abstract class introduces for storing all the information. Abstract class contains methods and attribute. All of them are describe below 

## Attributes

	type = None                         # type of the field (string)
    relational = False                  # whether the field is a relational one
    translate = False                   # whether the field is translated

    column_type = None                  # database column type (ident, spec)
    write_sequence = 0                  # field ordering for write()

    args = None                         # the parameters given to __init__()
    _module = None                      # the field's module name
    _modules = None                     # modules that define this field
    _setup_done = True                  # whether the field is completely set up
    _sequence = None                    # absolute ordering of the field
    _base_fields = ()                   # the fields defining self, in override order
    _extra_keys = ()                    # unknown attributes set on the field
    _direct = False                     # whether self may be used directly (shared)
    _toplevel = False                   # whether self is on the model's registry class

    automatic = False                   # whether the field is automatically created ("magic" field)
    inherited = False                   # whether the field is inherited (_inherits)
    inherited_field = None              # the corresponding inherited field

    name = None                         # name of the field
    model_name = None                   # name of the model of this field
    comodel_name = None                 # name of the model of values (if relational)

    store = True                        # whether the field is stored in database
    index = None                        # how the field is indexed in database
    manual = False                      # whether the field is a custom field
    copy = True                         # whether the field is copied over by BaseModel.copy()
    _depends = None                     # collection of field dependencies
    _depends_context = None             # collection of context key dependencies
    recursive = False                   # whether self depends on itself
    compute = None                      # compute(recs) computes field on recs
    compute_sudo = False                # whether field should be recomputed as superuser
    precompute = False                  # whether field has to be computed before creation
    inverse = None                      # inverse(recs) inverses field on recs
    search = None                       # search(recs, operator, value) searches on self
    related = None                      # sequence of field names, for related fields
    company_dependent = False           # whether ``self`` is company-dependent (property field)
    default = None                      # default(recs) returns the default value

    string = None                       # field label
    help = None                         # field tooltip
    invisible = False                   # whether the field is invisible
    readonly = False                    # whether the field is readonly
    required = False                    # whether the field is required
    states = None                       # set readonly and required depending on state
    groups = None                       # csv list of group xml ids
    change_default = False              # whether the field may trigger a "user-onchange"

    related_field = None                # corresponding related field
    group_operator = None               # operator for aggregating values
    group_expand = None                 # name of method to expand groups in read_group()
    prefetch = True                     # the prefetch group (False means no group)

    default_export_compatible = False   # whether the field must be exported by default in an import-compatible export
    exportable = True


## Field Types

All of field types are listed in short description

1. Boolean
2. Integer
3. Float
4. Monetary
5. Char
6. Text
7. Html
8. Date
9. Datetime
10. Binary
11. Image
12. Selection
13. Reference
14. Many2one
15. Many2oneReference
16. Json
17. Properties
18. PropertiesDefinition
19. One2many
20. Many2many


# API

Several decorator pattern

## constrains

Decorate a constraint checker.

Each argument must be a field name used in the check::

```
@api.constrains('name', 'description')
def _check_description(self):
    for record in self:
        if record.name == record.description:
           raise ValidationError("Fields name and description must be different")
```

Invoked on the records on which one of the named fields has been modified.

Should raise :exc:`~odoo.exceptions.ValidationError` if the validation failed.

### Warning
> `@constrains` only supports simple field names, dotted names
      (fields of relational fields e.g. ``partner_id.customer``) are not
        supported and will be ignored.
        

>`@constrains` will be triggered only if the declared fields in the
        decorated method are included in the ``create`` or ``write`` call.
        It implies that fields not present in a view will not trigger a call
        during a record creation. A override of ``create`` is necessary to make
        sure a constraint will always be triggered (e.g. to test the absence of
        value).

> One may also pass a single function as argument.  In that case, the field
    names are given by calling the function with a model instance.


## ondelete


Mark a method to be executed during :meth:`~odoo.models.BaseModel.unlink`.

The goal of this decorator is to allow client-side errors when unlinking
    records if, from a business point of view, it does not make sense to delete
    such records. For instance, a user should not be able to delete a validated
    sales order.

While this could be implemented by simply overriding the method ``unlink``
    on the model, it has the drawback of not being compatible with module
    uninstallation. When uninstalling the module, the override could raise user
    errors, but we shouldn't care because the module is being uninstalled, and
    thus **all** records related to the module should be removed anyway.

This means that by overriding ``unlink``, there is a big chance that some
    tables/records may remain as leftover data from the uninstalled module. This
    leaves the database in an inconsistent state. Moreover, there is a risk of
    conflicts if the module is ever reinstalled on that database.

Methods decorated with `@ondelete` should raise an error following some
    conditions, and by convention, the method should be named either

```
@api.ondelete(at_uninstall=False)
def _unlink_if_user_inactive(self):
     if any(user.active for user in self):
         raise UserError("Can't delete an active user!")

# same as above but with _unlink_except_* as method name
@api.ondelete(at_uninstall=False)
def _unlink_except_active_user(self):
    if any(user.active for user in self):
        raise UserError("Can't delete an active user!")
```

:param bool at_uninstall: Whether the decorated method should be called if
        the module that implements said method is being uninstalled. Should
        almost always be ``False``, so that module uninstallation does not
        trigger those errors.

### Warning
> The parameter ``at_uninstall`` should only be set to ``True`` if the
        check you are implementing also applies when uninstalling the module.

> For instance, it doesn't matter if when uninstalling ``sale``, validated
        sales orders are being deleted because all data pertaining to ``sale``
        should be deleted anyway, in that case ``at_uninstall`` should be set to
        ``False``.

> However, it makes sense to prevent the removal of the default language
        if no other languages are installed, since deleting the default language
        will break a lot of basic behavior. In this case, ``at_uninstall``
        should be set to ``True``.


## onchange

Return a decorator to decorate an onchange method for given fields.

    In the form views where the field appears, the method will be called
    when one of the given fields is modified. The method is invoked on a
    pseudo-record that contains the values present in the form. Field
    assignments on that record are automatically sent back to the client.

    Each argument must be a field name::

        @api.onchange('partner_id')
        def _onchange_partner(self):
            self.message = "Dear %s" % (self.partner_id.name or "")

    .. code-block:: python

        return {
            'warning': {'title': "Warning", 'message': "What is this?", 'type': 'notification'},
        }

    If the type is set to notification, the warning will be displayed in a notification.
    Otherwise it will be displayed in a dialog as default.

    .. warning::

        ``@onchange`` only supports simple field names, dotted names
        (fields of relational fields e.g. ``partner_id.tz``) are not
        supported and will be ignored

    .. danger::

        Since ``@onchange`` returns a recordset of pseudo-records,
        calling any one of the CRUD methods
        (:meth:`create`, :meth:`read`, :meth:`write`, :meth:`unlink`)
        on the aforementioned recordset is undefined behaviour,
        as they potentially do not exist in the database yet.

        Instead, simply set the record's field like shown in the example
        above or call the :meth:`update` method.

### Warning

> It is not possible for a ``one2many`` or ``many2many`` field to modify
        itself via onchange. This is a webclient limitation - see `#2693 <https://github.com/odoo/odoo/issues/2693>`_.


## depends
Return a decorator that specifies the field dependencies of a "compute"
        method (for new-style function fields). Each argument must be a string
        that consists in a dot-separated sequence of field names::

```
pname = fields.Char(compute='_compute_pname')


@api.depends('partner_id.name', 'partner_id.is_company')
def _compute_pname(self):
    for record in self:
        if record.partner_id.is_company:
            record.pname = (record.partner_id.name or "").upper()
        else:
            record.pname = record.partner_id.name

```           

One may also pass a single function as argument. In that case, the
        dependencies are given by calling the function with the field's model.


## depends_context
Return a decorator that specifies the context dependencies of a
    non-stored "compute" method.  Each argument is a key in the context's
    dictionary::

```
price = fields.Float(compute='_compute_product_price')


@api.depends_context('pricelist')
def _compute_product_price(self):
    for product in self:
        if product.env.context.get('pricelist'):
            pricelist = self.env['product.pricelist'].browse(product.env.context['pricelist'])
        else:
            pricelist = self.env['product.pricelist'].get_default_pricelist()
        product.price = pricelist._get_products_price(product).get(product.id, 0.0)

```

All dependencies must be hashable.  The following keys have special
    support:

    * `company` (value in context or current company id),
    * `uid` (current user id and superuser flag),
    * `active_test` (value in env.context or value in field.context).




## returns
Return a decorator for methods that return instances of ``model``.

`:param` model: a model name, or ``'self'`` for the current model

`:param` downgrade: a function ``downgrade(self, value, *args, **kwargs)``
            to convert the record-style ``value`` to a traditional-style output

`:param` upgrade: a function ``upgrade(self, value, *args, **kwargs)``
            to convert the traditional-style ``value`` to a record-style output

The arguments ``self``, ``*args`` and ``**kwargs`` are the ones passed
        to the method in the record-style.

The decorator adapts the method output to the api style: ``id``, ``ids`` or
        ``False`` for the traditional style, and recordset for the record style::

```
@model
@returns('res.partner')
def find_partner(self, arg):
    ...  # return some record


# output depends on call style: traditional vs record style
partner_id = model.find_partner(cr, uid, arg, context=context)

# recs = model.browse(cr, uid, ids, context)
partner_record = recs.find_partner(arg)

```

Note that the decorated method must satisfy that convention.

Those decorators are automatically *inherited*: a method that overrides
        a decorated existing method will be decorated with the same
        ``@returns(model)``.


## downgrade

Convert ``value`` returned by ``method`` on ``self`` to traditional style.


## split_context
Extract the context from a pair of positional and keyword arguments.
        Return a triple ``context, args, kwargs``.

## autovacuum
Decorate a method so that it is called by the daily vacuum cron job (model
    ``ir.autovacuum``).  This is typically used for garbage-collection-like
    tasks that do not deserve a specific cron job.

## model

Decorate a record-style method where ``self`` is a recordset, but its
        contents is not relevant, only the model is. Such a method::
```
@api.model
def method(self, args):
	...
```

## model_create_single
Decorate a method that takes a dictionary and creates a single record.
        The method may be called with either a single dict or a list of dicts::

```
record = model.create(vals)
records = model.create([vals, ...])
```

## model_create_multi
Decorate a method that takes a list of dictionaries and creates multiple
        records. The method may be called with either a single dict or a list of
        dicts::

```
record = model.create(vals)
records = model.create([vals, ...])
```


## call_kw
Invoke the given method `name` on the recordset `model`.



# Exceptions

Those types are understood by the RPC layer.
Any other exception type bubbling until the RPC layer will be
treated as a 'Server error'.

> note::
    If you consider introducing new exceptions,
    check out the :mod:`odoo.addons.test_exceptions` module.


There are few exceptions available in odoo
Exceptions are depends on python packages `warnings`.

There are 7 exceptions are available in odoo 
1. UserError
2. RedirectWarning
3. AccessDenied
4. AccessError
5. CacheMiss
6. MissingError
7. ValidationError


Details of Exceptions are given

## 1. UserError

Generic error managed by the client.


Typically when the user tries to do something that has no sense given the current
state of a record. Semantically comparable to the generic 400 HTTP status codes.

```
from odoo.exceptions import UserError

raise UserError("UserError attribute 'name' is a deprecated alias to args")

```

## 2. RedirectWarning
Warning with a possibility to redirect the user instead of simply
    displaying the warning message.

`:param` str message: exception message and frontend modal content  
`:param` int action_id: id of the action where to perform the redirection  
`:param` str button_text: text to put on the button that will trigger the redirection.  
`:param` dict additional_context: parameter passed to action_id.
           Can be used to limit a view to active_ids for example.


```
from odoo.exceptions import RedirectWarning

raise RedirectWarning("UserError attribute 'name' is a deprecated alias to args")

```


## 3. AccessDenied
Login/password error.

> note:: No traceback.

> admonition:: Example When you try to log with a wrong password.

## 4. AccessError
Access rights error.

> admonition:: Example  
When you try to read a record that you are not allowed to.


## 5. CacheMiss
Missing value(s) in cache.

> admonition:: Example  
        When you try to read a value in a flushed cache.


## 6. MissingError
Missing record(s).

> admonition:: Example  
  When you try to write on a deleted record.

```
from odoo.exceptions import MissingError

raise MissingError("MissingError attribute 'name' is a deprecated alias to args")
```


## 7. ValidationError

Violation of python constraints.

> admonition:: Example   
When you try to create a new user with a login which already exist in the db.

```
from odoo.exceptions import ValidationError

raise ValidationError("ValidationError attribute 'name' is a deprecated alias to args")
```










































