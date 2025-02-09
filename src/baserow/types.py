
import dataclasses
import enum
import typing as t

from databind.core.settings import Union

T = t.TypeVar('T')


class Permissions(enum.Enum):
  MEMBER = enum.auto()
  ADMIN = enum.auto()


@dataclasses.dataclass
class User:
  id: int
  first_name: str
  username: str
  is_staff: bool
  language: str


@dataclasses.dataclass
class Group:
  id: int
  name: str

@dataclasses.dataclass
class Workspace:
  id: int
  name: str

@dataclasses.dataclass
class OrderedGroup(Group):
  order: int


@dataclasses.dataclass
class PermissionedOrderedGroup(OrderedGroup):
  permissions: Permissions


@dataclasses.dataclass
class Table:
  id: int
  name: str
  order: int
  database_id: int


@Union(style=Union.FLAT)
@dataclasses.dataclass
class TableField:
  id: int
  table_id: int
  name: str
  order: int
  primary: bool
  read_only: bool


@dataclasses.dataclass
class Application:
  id: int
  name: str
  order: int
  type: str
  workspace: Workspace
  tables: t.List[Table]
  group: t.Optional[Group] = None


@dataclasses.dataclass
class Page(t.Generic[T]):
  count: int
  previous: t.Optional[int]
  next: t.Optional[int]
  results: t.List[T]


from . import field_types
