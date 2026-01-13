export const AlertTypes = {
  INFO: "text-fg-brand-strong",
  INFO_BG: "bg-brand-softer",
  DANGER: "text-fg-danger-strong",
  DANGER_BG: "bg-danger-soft",
  SUCCESS: "text-fg-success-strong",
  SUCCESS_BG: "bg-success-soft",
  WARNING: "text-fg-warning",
  WARNING_BG: "bg-warning-soft",
  REGULAR: "text-heading",
  REGULAR_BG: "bg-neutral-secondary-medium",
} as const;

export const ALERT_PRESETS = {
  danger: {
    color: AlertTypes.DANGER,
    bgColor: AlertTypes.DANGER_BG,
  },
  success: {
    color: AlertTypes.SUCCESS,
    bgColor: AlertTypes.SUCCESS_BG,
  },
  warning: {
    color: AlertTypes.WARNING,
    bgColor: AlertTypes.WARNING_BG,
  },
  info: {
    color: AlertTypes.INFO,
    bgColor: AlertTypes.INFO_BG,
  },
  regular: {
    color: AlertTypes.REGULAR,
    bgColor: AlertTypes.REGULAR_BG,
  },
} as const;

export type AlertColor = (typeof AlertTypes)[keyof typeof AlertTypes];

export type AlertType = {
  id: number;
  color: AlertColor;
  bgColor: AlertColor;
  message: string;
};
