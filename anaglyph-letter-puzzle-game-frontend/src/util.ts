/**
 * removes keys from `keys` specfied in `toRemove`
 * @param keys inital key array (string array)
 * @param toRemove keys to be removed
 * @returns new array with keys removed
 */
export function filterUserData(keys: string[], toRemove: string[] = ["creator", "lastUpdated", "created", "username", "notes"]) {
    const __keys = [...keys];

    // remove all keys from toRemove
    toRemove.forEach((rm) => {
        const index = __keys.findIndex((key) => key === rm);
        if (index >= 0) {
            __keys.splice(index, 1);
        }
    });

    return __keys;
}

/**
 * makes it so the the keys specfied in `order` appear first and in that order
 * @param keys keys to be reorderd
 * @param order the ordering you want
 * @returns ordered array
 */
export function reorderUserData(keys: string[], order = ["password"]) {
    const __keys = filterUserData(keys, order);
    return [...order].concat(__keys);
}

/**
 * see `filterUserData` and `reorderUserData`
 */
export function filterAndReorderUserData(keys: string[]) {
    let __keys: string[];

    __keys = filterUserData(keys);
    __keys = reorderUserData(__keys);

    return __keys;
}
