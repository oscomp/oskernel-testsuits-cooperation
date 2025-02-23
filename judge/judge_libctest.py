import json
import sys

libctest_baseline = """
========== START entry-static.exe argv ==========
Pass!
========== END entry-static.exe argv ==========
========== START entry-static.exe basename ==========
Pass!
========== END entry-static.exe basename ==========
========== START entry-static.exe clocale_mbfuncs ==========
Pass!
========== END entry-static.exe clocale_mbfuncs ==========
========== START entry-static.exe clock_gettime ==========
Pass!
========== END entry-static.exe clock_gettime ==========
========== START entry-static.exe crypt ==========
Pass!
========== END entry-static.exe crypt ==========
========== START entry-static.exe dirname ==========
Pass!
========== END entry-static.exe dirname ==========
========== START entry-static.exe env ==========
Pass!
========== END entry-static.exe env ==========
========== START entry-static.exe fdopen ==========
Pass!
========== END entry-static.exe fdopen ==========
========== START entry-static.exe fnmatch ==========
Pass!
========== END entry-static.exe fnmatch ==========
========== START entry-static.exe fscanf ==========
Pass!
========== END entry-static.exe fscanf ==========
========== START entry-static.exe fwscanf ==========
Pass!
========== END entry-static.exe fwscanf ==========
========== START entry-static.exe iconv_open ==========
Pass!
========== END entry-static.exe iconv_open ==========
========== START entry-static.exe inet_pton ==========
Pass!
========== END entry-static.exe inet_pton ==========
========== START entry-static.exe mbc ==========
Pass!
========== END entry-static.exe mbc ==========
========== START entry-static.exe memstream ==========
Pass!
========== END entry-static.exe memstream ==========
========== START entry-static.exe pthread_cancel_points ==========
Pass!
========== END entry-static.exe pthread_cancel_points ==========
========== START entry-static.exe pthread_cancel ==========
Pass!
========== END entry-static.exe pthread_cancel ==========
========== START entry-static.exe pthread_cond ==========
Pass!
========== END entry-static.exe pthread_cond ==========
========== START entry-static.exe pthread_tsd ==========
Pass!
========== END entry-static.exe pthread_tsd ==========
========== START entry-static.exe qsort ==========
Pass!
========== END entry-static.exe qsort ==========
========== START entry-static.exe random ==========
Pass!
========== END entry-static.exe random ==========
========== START entry-static.exe search_hsearch ==========
Pass!
========== END entry-static.exe search_hsearch ==========
========== START entry-static.exe search_insque ==========
Pass!
========== END entry-static.exe search_insque ==========
========== START entry-static.exe search_lsearch ==========
Pass!
========== END entry-static.exe search_lsearch ==========
========== START entry-static.exe search_tsearch ==========
Pass!
========== END entry-static.exe search_tsearch ==========
========== START entry-static.exe setjmp ==========
Pass!
========== END entry-static.exe setjmp ==========
========== START entry-static.exe snprintf ==========
Pass!
========== END entry-static.exe snprintf ==========
========== START entry-static.exe socket ==========
Pass!
========== END entry-static.exe socket ==========
========== START entry-static.exe sscanf ==========
Pass!
========== END entry-static.exe sscanf ==========
========== START entry-static.exe sscanf_long ==========
Pass!
========== END entry-static.exe sscanf_long ==========
========== START entry-static.exe stat ==========
Pass!
========== END entry-static.exe stat ==========
========== START entry-static.exe strftime ==========
Pass!
========== END entry-static.exe strftime ==========
========== START entry-static.exe string ==========
Pass!
========== END entry-static.exe string ==========
========== START entry-static.exe string_memcpy ==========
Pass!
========== END entry-static.exe string_memcpy ==========
========== START entry-static.exe string_memmem ==========
Pass!
========== END entry-static.exe string_memmem ==========
========== START entry-static.exe string_memset ==========
Pass!
========== END entry-static.exe string_memset ==========
========== START entry-static.exe string_strchr ==========
Pass!
========== END entry-static.exe string_strchr ==========
========== START entry-static.exe string_strcspn ==========
Pass!
========== END entry-static.exe string_strcspn ==========
========== START entry-static.exe string_strstr ==========
Pass!
========== END entry-static.exe string_strstr ==========
========== START entry-static.exe strptime ==========
Pass!
========== END entry-static.exe strptime ==========
========== START entry-static.exe strtod ==========
Pass!
========== END entry-static.exe strtod ==========
========== START entry-static.exe strtod_simple ==========
Pass!
========== END entry-static.exe strtod_simple ==========
========== START entry-static.exe strtof ==========
Pass!
========== END entry-static.exe strtof ==========
========== START entry-static.exe strtol ==========
Pass!
========== END entry-static.exe strtol ==========
========== START entry-static.exe strtold ==========
Pass!
========== END entry-static.exe strtold ==========
========== START entry-static.exe swprintf ==========
Pass!
========== END entry-static.exe swprintf ==========
========== START entry-static.exe tgmath ==========
Pass!
========== END entry-static.exe tgmath ==========
========== START entry-static.exe time ==========
Pass!
========== END entry-static.exe time ==========
========== START entry-static.exe tls_align ==========
Pass!
========== END entry-static.exe tls_align ==========
========== START entry-static.exe udiv ==========
Pass!
========== END entry-static.exe udiv ==========
========== START entry-static.exe ungetc ==========
Pass!
========== END entry-static.exe ungetc ==========
========== START entry-static.exe utime ==========
Pass!
========== END entry-static.exe utime ==========
========== START entry-static.exe wcsstr ==========
Pass!
========== END entry-static.exe wcsstr ==========
========== START entry-static.exe wcstol ==========
Pass!
========== END entry-static.exe wcstol ==========
========== START entry-static.exe pleval ==========
Pass!
========== END entry-static.exe pleval ==========
========== START entry-static.exe daemon_failure ==========
Pass!
========== END entry-static.exe daemon_failure ==========
========== START entry-static.exe dn_expand_empty ==========
Pass!
========== END entry-static.exe dn_expand_empty ==========
========== START entry-static.exe dn_expand_ptr_0 ==========
Pass!
========== END entry-static.exe dn_expand_ptr_0 ==========
========== START entry-static.exe fflush_exit ==========
Pass!
========== END entry-static.exe fflush_exit ==========
========== START entry-static.exe fgets_eof ==========
Pass!
========== END entry-static.exe fgets_eof ==========
========== START entry-static.exe fgetwc_buffering ==========
Pass!
========== END entry-static.exe fgetwc_buffering ==========
========== START entry-static.exe fpclassify_invalid_ld80 ==========
Pass!
========== END entry-static.exe fpclassify_invalid_ld80 ==========
========== START entry-static.exe ftello_unflushed_append ==========
Pass!
========== END entry-static.exe ftello_unflushed_append ==========
========== START entry-static.exe getpwnam_r_crash ==========
Pass!
========== END entry-static.exe getpwnam_r_crash ==========
========== START entry-static.exe getpwnam_r_errno ==========
Pass!
========== END entry-static.exe getpwnam_r_errno ==========
========== START entry-static.exe iconv_roundtrips ==========
Pass!
========== END entry-static.exe iconv_roundtrips ==========
========== START entry-static.exe inet_ntop_v4mapped ==========
Pass!
========== END entry-static.exe inet_ntop_v4mapped ==========
========== START entry-static.exe inet_pton_empty_last_field ==========
Pass!
========== END entry-static.exe inet_pton_empty_last_field ==========
========== START entry-static.exe iswspace_null ==========
Pass!
========== END entry-static.exe iswspace_null ==========
========== START entry-static.exe lrand48_signextend ==========
Pass!
========== END entry-static.exe lrand48_signextend ==========
========== START entry-static.exe lseek_large ==========
Pass!
========== END entry-static.exe lseek_large ==========
========== START entry-static.exe malloc_0 ==========
Pass!
========== END entry-static.exe malloc_0 ==========
========== START entry-static.exe mbsrtowcs_overflow ==========
Pass!
========== END entry-static.exe mbsrtowcs_overflow ==========
========== START entry-static.exe memmem_oob_read ==========
Pass!
========== END entry-static.exe memmem_oob_read ==========
========== START entry-static.exe memmem_oob ==========
Pass!
========== END entry-static.exe memmem_oob ==========
========== START entry-static.exe mkdtemp_failure ==========
Pass!
========== END entry-static.exe mkdtemp_failure ==========
========== START entry-static.exe mkstemp_failure ==========
Pass!
========== END entry-static.exe mkstemp_failure ==========
========== START entry-static.exe printf_1e9_oob ==========
Pass!
========== END entry-static.exe printf_1e9_oob ==========
========== START entry-static.exe printf_fmt_g_round ==========
Pass!
========== END entry-static.exe printf_fmt_g_round ==========
========== START entry-static.exe printf_fmt_g_zeros ==========
Pass!
========== END entry-static.exe printf_fmt_g_zeros ==========
========== START entry-static.exe printf_fmt_n ==========
Pass!
========== END entry-static.exe printf_fmt_n ==========
========== START entry-static.exe pthread_robust_detach ==========
Pass!
========== END entry-static.exe pthread_robust_detach ==========
========== START entry-static.exe pthread_cancel_sem_wait ==========
Pass!
========== END entry-static.exe pthread_cancel_sem_wait ==========
========== START entry-static.exe pthread_cond_smasher ==========
Pass!
========== END entry-static.exe pthread_cond_smasher ==========
========== START entry-static.exe pthread_condattr_setclock ==========
Pass!
========== END entry-static.exe pthread_condattr_setclock ==========
========== START entry-static.exe pthread_exit_cancel ==========
Pass!
========== END entry-static.exe pthread_exit_cancel ==========
========== START entry-static.exe pthread_once_deadlock ==========
Pass!
========== END entry-static.exe pthread_once_deadlock ==========
========== START entry-static.exe pthread_rwlock_ebusy ==========
Pass!
========== END entry-static.exe pthread_rwlock_ebusy ==========
========== START entry-static.exe putenv_doublefree ==========
Pass!
========== END entry-static.exe putenv_doublefree ==========
========== START entry-static.exe regex_backref_0 ==========
Pass!
========== END entry-static.exe regex_backref_0 ==========
========== START entry-static.exe regex_bracket_icase ==========
Pass!
========== END entry-static.exe regex_bracket_icase ==========
========== START entry-static.exe regex_ere_backref ==========
Pass!
========== END entry-static.exe regex_ere_backref ==========
========== START entry-static.exe regex_escaped_high_byte ==========
Pass!
========== END entry-static.exe regex_escaped_high_byte ==========
========== START entry-static.exe regex_negated_range ==========
Pass!
========== END entry-static.exe regex_negated_range ==========
========== START entry-static.exe regexec_nosub ==========
Pass!
========== END entry-static.exe regexec_nosub ==========
========== START entry-static.exe rewind_clear_error ==========
Pass!
========== END entry-static.exe rewind_clear_error ==========
========== START entry-static.exe rlimit_open_files ==========
Pass!
========== END entry-static.exe rlimit_open_files ==========
========== START entry-static.exe scanf_bytes_consumed ==========
Pass!
========== END entry-static.exe scanf_bytes_consumed ==========
========== START entry-static.exe scanf_match_literal_eof ==========
Pass!
========== END entry-static.exe scanf_match_literal_eof ==========
========== START entry-static.exe scanf_nullbyte_char ==========
Pass!
========== END entry-static.exe scanf_nullbyte_char ==========
========== START entry-static.exe setvbuf_unget ==========
Pass!
========== END entry-static.exe setvbuf_unget ==========
========== START entry-static.exe sigprocmask_internal ==========
Pass!
========== END entry-static.exe sigprocmask_internal ==========
========== START entry-static.exe sscanf_eof ==========
Pass!
========== END entry-static.exe sscanf_eof ==========
========== START entry-static.exe statvfs ==========
Pass!
========== END entry-static.exe statvfs ==========
========== START entry-static.exe strverscmp ==========
Pass!
========== END entry-static.exe strverscmp ==========
========== START entry-static.exe syscall_sign_extend ==========
Pass!
========== END entry-static.exe syscall_sign_extend ==========
========== START entry-static.exe uselocale_0 ==========
Pass!
========== END entry-static.exe uselocale_0 ==========
========== START entry-static.exe wcsncpy_read_overflow ==========
Pass!
========== END entry-static.exe wcsncpy_read_overflow ==========
========== START entry-static.exe wcsstr_false_negative ==========
Pass!
========== END entry-static.exe wcsstr_false_negative ==========
========== START entry-dynamic.exe argv ==========
Pass!
========== END entry-dynamic.exe argv ==========
========== START entry-dynamic.exe basename ==========
Pass!
========== END entry-dynamic.exe basename ==========
========== START entry-dynamic.exe clocale_mbfuncs ==========
Pass!
========== END entry-dynamic.exe clocale_mbfuncs ==========
========== START entry-dynamic.exe clock_gettime ==========
Pass!
========== END entry-dynamic.exe clock_gettime ==========
========== START entry-dynamic.exe crypt ==========
Pass!
========== END entry-dynamic.exe crypt ==========
========== START entry-dynamic.exe dirname ==========
Pass!
========== END entry-dynamic.exe dirname ==========
========== START entry-dynamic.exe dlopen ==========
Pass!
========== END entry-dynamic.exe dlopen ==========
========== START entry-dynamic.exe env ==========
Pass!
========== END entry-dynamic.exe env ==========
========== START entry-dynamic.exe fdopen ==========
Pass!
========== END entry-dynamic.exe fdopen ==========
========== START entry-dynamic.exe fnmatch ==========
Pass!
========== END entry-dynamic.exe fnmatch ==========
========== START entry-dynamic.exe fscanf ==========
Pass!
========== END entry-dynamic.exe fscanf ==========
========== START entry-dynamic.exe fwscanf ==========
Pass!
========== END entry-dynamic.exe fwscanf ==========
========== START entry-dynamic.exe iconv_open ==========
Pass!
========== END entry-dynamic.exe iconv_open ==========
========== START entry-dynamic.exe inet_pton ==========
Pass!
========== END entry-dynamic.exe inet_pton ==========
========== START entry-dynamic.exe mbc ==========
Pass!
========== END entry-dynamic.exe mbc ==========
========== START entry-dynamic.exe memstream ==========
Pass!
========== END entry-dynamic.exe memstream ==========
========== START entry-dynamic.exe pthread_cancel_points ==========
Pass!
========== END entry-dynamic.exe pthread_cancel_points ==========
========== START entry-dynamic.exe pthread_cancel ==========
Pass!
========== END entry-dynamic.exe pthread_cancel ==========
========== START entry-dynamic.exe pthread_cond ==========
Pass!
========== END entry-dynamic.exe pthread_cond ==========
========== START entry-dynamic.exe pthread_tsd ==========
Pass!
========== END entry-dynamic.exe pthread_tsd ==========
========== START entry-dynamic.exe qsort ==========
Pass!
========== END entry-dynamic.exe qsort ==========
========== START entry-dynamic.exe random ==========
Pass!
========== END entry-dynamic.exe random ==========
========== START entry-dynamic.exe search_hsearch ==========
Pass!
========== END entry-dynamic.exe search_hsearch ==========
========== START entry-dynamic.exe search_insque ==========
Pass!
========== END entry-dynamic.exe search_insque ==========
========== START entry-dynamic.exe search_lsearch ==========
Pass!
========== END entry-dynamic.exe search_lsearch ==========
========== START entry-dynamic.exe search_tsearch ==========
Pass!
========== END entry-dynamic.exe search_tsearch ==========
========== START entry-dynamic.exe sem_init ==========
Pass!
========== END entry-dynamic.exe sem_init ==========
========== START entry-dynamic.exe setjmp ==========
Pass!
========== END entry-dynamic.exe setjmp ==========
========== START entry-dynamic.exe snprintf ==========
Pass!
========== END entry-dynamic.exe snprintf ==========
========== START entry-dynamic.exe socket ==========
Pass!
========== END entry-dynamic.exe socket ==========
========== START entry-dynamic.exe sscanf ==========
Pass!
========== END entry-dynamic.exe sscanf ==========
========== START entry-dynamic.exe sscanf_long ==========
Pass!
========== END entry-dynamic.exe sscanf_long ==========
========== START entry-dynamic.exe stat ==========
Pass!
========== END entry-dynamic.exe stat ==========
========== START entry-dynamic.exe strftime ==========
Pass!
========== END entry-dynamic.exe strftime ==========
========== START entry-dynamic.exe string ==========
Pass!
========== END entry-dynamic.exe string ==========
========== START entry-dynamic.exe string_memcpy ==========
Pass!
========== END entry-dynamic.exe string_memcpy ==========
========== START entry-dynamic.exe string_memmem ==========
Pass!
========== END entry-dynamic.exe string_memmem ==========
========== START entry-dynamic.exe string_memset ==========
Pass!
========== END entry-dynamic.exe string_memset ==========
========== START entry-dynamic.exe string_strchr ==========
Pass!
========== END entry-dynamic.exe string_strchr ==========
========== START entry-dynamic.exe string_strcspn ==========
Pass!
========== END entry-dynamic.exe string_strcspn ==========
========== START entry-dynamic.exe string_strstr ==========
Pass!
========== END entry-dynamic.exe string_strstr ==========
========== START entry-dynamic.exe strptime ==========
Pass!
========== END entry-dynamic.exe strptime ==========
========== START entry-dynamic.exe strtod ==========
Pass!
========== END entry-dynamic.exe strtod ==========
========== START entry-dynamic.exe strtod_simple ==========
Pass!
========== END entry-dynamic.exe strtod_simple ==========
========== START entry-dynamic.exe strtof ==========
Pass!
========== END entry-dynamic.exe strtof ==========
========== START entry-dynamic.exe strtol ==========
Pass!
========== END entry-dynamic.exe strtol ==========
========== START entry-dynamic.exe strtold ==========
Pass!
========== END entry-dynamic.exe strtold ==========
========== START entry-dynamic.exe swprintf ==========
Pass!
========== END entry-dynamic.exe swprintf ==========
========== START entry-dynamic.exe tgmath ==========
Pass!
========== END entry-dynamic.exe tgmath ==========
========== START entry-dynamic.exe time ==========
Pass!
========== END entry-dynamic.exe time ==========
========== START entry-dynamic.exe tls_init ==========
Pass!
========== END entry-dynamic.exe tls_init ==========
========== START entry-dynamic.exe tls_local_exec ==========
Pass!
========== END entry-dynamic.exe tls_local_exec ==========
========== START entry-dynamic.exe udiv ==========
Pass!
========== END entry-dynamic.exe udiv ==========
========== START entry-dynamic.exe ungetc ==========
Pass!
========== END entry-dynamic.exe ungetc ==========
========== START entry-dynamic.exe utime ==========
Pass!
========== END entry-dynamic.exe utime ==========
========== START entry-dynamic.exe wcsstr ==========
Pass!
========== END entry-dynamic.exe wcsstr ==========
========== START entry-dynamic.exe wcstol ==========
Pass!
========== END entry-dynamic.exe wcstol ==========
========== START entry-dynamic.exe daemon_failure ==========
Pass!
========== END entry-dynamic.exe daemon_failure ==========
========== START entry-dynamic.exe dn_expand_empty ==========
Pass!
========== END entry-dynamic.exe dn_expand_empty ==========
========== START entry-dynamic.exe dn_expand_ptr_0 ==========
Pass!
========== END entry-dynamic.exe dn_expand_ptr_0 ==========
========== START entry-dynamic.exe fflush_exit ==========
Pass!
========== END entry-dynamic.exe fflush_exit ==========
========== START entry-dynamic.exe fgets_eof ==========
Pass!
========== END entry-dynamic.exe fgets_eof ==========
========== START entry-dynamic.exe fgetwc_buffering ==========
Pass!
========== END entry-dynamic.exe fgetwc_buffering ==========
========== START entry-dynamic.exe fpclassify_invalid_ld80 ==========
Pass!
========== END entry-dynamic.exe fpclassify_invalid_ld80 ==========
========== START entry-dynamic.exe ftello_unflushed_append ==========
Pass!
========== END entry-dynamic.exe ftello_unflushed_append ==========
========== START entry-dynamic.exe getpwnam_r_crash ==========
Pass!
========== END entry-dynamic.exe getpwnam_r_crash ==========
========== START entry-dynamic.exe getpwnam_r_errno ==========
Pass!
========== END entry-dynamic.exe getpwnam_r_errno ==========
========== START entry-dynamic.exe iconv_roundtrips ==========
Pass!
========== END entry-dynamic.exe iconv_roundtrips ==========
========== START entry-dynamic.exe inet_ntop_v4mapped ==========
Pass!
========== END entry-dynamic.exe inet_ntop_v4mapped ==========
========== START entry-dynamic.exe inet_pton_empty_last_field ==========
Pass!
========== END entry-dynamic.exe inet_pton_empty_last_field ==========
========== START entry-dynamic.exe iswspace_null ==========
Pass!
========== END entry-dynamic.exe iswspace_null ==========
========== START entry-dynamic.exe lrand48_signextend ==========
Pass!
========== END entry-dynamic.exe lrand48_signextend ==========
========== START entry-dynamic.exe lseek_large ==========
Pass!
========== END entry-dynamic.exe lseek_large ==========
========== START entry-dynamic.exe malloc_0 ==========
Pass!
========== END entry-dynamic.exe malloc_0 ==========
========== START entry-dynamic.exe mbsrtowcs_overflow ==========
Pass!
========== END entry-dynamic.exe mbsrtowcs_overflow ==========
========== START entry-dynamic.exe memmem_oob_read ==========
Pass!
========== END entry-dynamic.exe memmem_oob_read ==========
========== START entry-dynamic.exe memmem_oob ==========
Pass!
========== END entry-dynamic.exe memmem_oob ==========
========== START entry-dynamic.exe mkdtemp_failure ==========
Pass!
========== END entry-dynamic.exe mkdtemp_failure ==========
========== START entry-dynamic.exe mkstemp_failure ==========
Pass!
========== END entry-dynamic.exe mkstemp_failure ==========
========== START entry-dynamic.exe printf_1e9_oob ==========
Pass!
========== END entry-dynamic.exe printf_1e9_oob ==========
========== START entry-dynamic.exe printf_fmt_g_round ==========
Pass!
========== END entry-dynamic.exe printf_fmt_g_round ==========
========== START entry-dynamic.exe printf_fmt_g_zeros ==========
Pass!
========== END entry-dynamic.exe printf_fmt_g_zeros ==========
========== START entry-dynamic.exe printf_fmt_n ==========
Pass!
========== END entry-dynamic.exe printf_fmt_n ==========
========== START entry-dynamic.exe pthread_robust_detach ==========
Pass!
========== END entry-dynamic.exe pthread_robust_detach ==========
========== START entry-dynamic.exe pthread_cond_smasher ==========
Pass!
========== END entry-dynamic.exe pthread_cond_smasher ==========
========== START entry-dynamic.exe pthread_condattr_setclock ==========
Pass!
========== END entry-dynamic.exe pthread_condattr_setclock ==========
========== START entry-dynamic.exe pthread_exit_cancel ==========
Pass!
========== END entry-dynamic.exe pthread_exit_cancel ==========
========== START entry-dynamic.exe pthread_once_deadlock ==========
Pass!
========== END entry-dynamic.exe pthread_once_deadlock ==========
========== START entry-dynamic.exe pthread_rwlock_ebusy ==========
Pass!
========== END entry-dynamic.exe pthread_rwlock_ebusy ==========
========== START entry-dynamic.exe putenv_doublefree ==========
Pass!
========== END entry-dynamic.exe putenv_doublefree ==========
========== START entry-dynamic.exe regex_backref_0 ==========
Pass!
========== END entry-dynamic.exe regex_backref_0 ==========
========== START entry-dynamic.exe regex_bracket_icase ==========
Pass!
========== END entry-dynamic.exe regex_bracket_icase ==========
========== START entry-dynamic.exe regex_ere_backref ==========
Pass!
========== END entry-dynamic.exe regex_ere_backref ==========
========== START entry-dynamic.exe regex_escaped_high_byte ==========
Pass!
========== END entry-dynamic.exe regex_escaped_high_byte ==========
========== START entry-dynamic.exe regex_negated_range ==========
Pass!
========== END entry-dynamic.exe regex_negated_range ==========
========== START entry-dynamic.exe regexec_nosub ==========
Pass!
========== END entry-dynamic.exe regexec_nosub ==========
========== START entry-dynamic.exe rewind_clear_error ==========
Pass!
========== END entry-dynamic.exe rewind_clear_error ==========
========== START entry-dynamic.exe rlimit_open_files ==========
Pass!
========== END entry-dynamic.exe rlimit_open_files ==========
========== START entry-dynamic.exe scanf_bytes_consumed ==========
Pass!
========== END entry-dynamic.exe scanf_bytes_consumed ==========
========== START entry-dynamic.exe scanf_match_literal_eof ==========
Pass!
========== END entry-dynamic.exe scanf_match_literal_eof ==========
========== START entry-dynamic.exe scanf_nullbyte_char ==========
Pass!
========== END entry-dynamic.exe scanf_nullbyte_char ==========
========== START entry-dynamic.exe setvbuf_unget ==========
Pass!
========== END entry-dynamic.exe setvbuf_unget ==========
========== START entry-dynamic.exe sigprocmask_internal ==========
Pass!
========== END entry-dynamic.exe sigprocmask_internal ==========
========== START entry-dynamic.exe sscanf_eof ==========
Pass!
========== END entry-dynamic.exe sscanf_eof ==========
========== START entry-dynamic.exe statvfs ==========
Pass!
========== END entry-dynamic.exe statvfs ==========
========== START entry-dynamic.exe strverscmp ==========
Pass!
========== END entry-dynamic.exe strverscmp ==========
========== START entry-dynamic.exe syscall_sign_extend ==========
Pass!
========== END entry-dynamic.exe syscall_sign_extend ==========
========== START entry-dynamic.exe tls_get_new_dtv ==========
Pass!
========== END entry-dynamic.exe tls_get_new_dtv ==========
========== START entry-dynamic.exe uselocale_0 ==========
Pass!
========== END entry-dynamic.exe uselocale_0 ==========
========== START entry-dynamic.exe wcsncpy_read_overflow ==========
Pass!
========== END entry-dynamic.exe wcsncpy_read_overflow ==========
========== START entry-dynamic.exe wcsstr_false_negative ==========
Pass!
========== END entry-dynamic.exe wcsstr_false_negative ==========
"""

def parse_libctest(output):
    ans = {}
    key = ""
    for line in output.split("\n"):
        if "START entry-static.exe" in line:
            key = "libctest static " + line.split(" ")[3]
        elif "START entry-dynamic.exe" in line:
            key = "libctest dynamic " + line.split(" ")[3]
        if line == "Pass!" and key != "":
            ans[key] = 1
    return ans

serial_out = sys.stdin.read()
libctest_baseline_out = parse_libctest(libctest_baseline)
libctest_output = parse_libctest(serial_out)
for k in libctest_baseline_out.keys():
    if k not in libctest_output:
        libctest_output[k] = 0

results = [{
    "name": k,
    "pass": v,
    "total": 1,
    "score": v,
} for k, v in libctest_output.items()]
print(json.dumps(results))
