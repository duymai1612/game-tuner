//! C ABI wrapper over the MIT `oozextract` Oodle decoder, for pbz_save_tool.py.
//! Decode only: the tool writes Oodle "stored" blocks, which need no encoder.
use std::{panic::catch_unwind, panic::AssertUnwindSafe, slice};

const MAX: usize = 64 * 1024 * 1024;

/// Returns `dst_len` on success, a negative value on any failure.
///
/// # Safety
/// `src` and `dst` must be valid, non-overlapping buffers of the given lengths.
#[no_mangle]
pub unsafe extern "C" fn pbz_decode(src: *const u8, src_len: usize, dst: *mut u8, dst_len: usize) -> isize {
    if src.is_null() || dst.is_null() || src_len == 0 || src_len > MAX + 65536 || dst_len > MAX {
        return -1;
    }
    let input = slice::from_raw_parts(src, src_len);
    let output = slice::from_raw_parts_mut(dst, dst_len);
    match catch_unwind(AssertUnwindSafe(|| oozextract::Extractor::new().read_from_slice(input, output))) {
        Ok(Ok(n)) if n == dst_len => n as isize,
        Ok(_) => -2,
        Err(_) => -3,
    }
}
