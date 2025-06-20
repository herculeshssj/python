import { Permission, PermissionDetail } from "./Permission";

export type Group = {
    id: number;
    name: string;
}

export type GroupDetail = Group & {
    permissions: Permission[]
}

export type ApiGetGroups = {
    groups: GroupDetail[]
}

export type ApiGetGroup = {
    permissions: PermissionDetail[]
}